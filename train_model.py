import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import (
    ModelCheckpoint,
    EarlyStopping,
    ReduceLROnPlateau
)
from sklearn.utils.class_weight import compute_class_weight
import numpy as np

# =========================
# SETTINGS
# =========================

IMG_SIZE = 224
BATCH_SIZE = 16

DATASET_DIR = "training_dataset"
MODEL_SAVE_PATH = "mobilenetv2_crop_disease.h5"

INITIAL_EPOCHS = 15
FINE_TUNE_EPOCHS = 15

# =========================
# DATA GENERATORS
# =========================

train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    validation_split=0.2,

    rotation_range=25,
    width_shift_range=0.15,
    height_shift_range=0.15,
    zoom_range=0.20,
    shear_range=0.10,
    horizontal_flip=True,
    brightness_range=[0.8, 1.2],
    fill_mode="nearest"
)

val_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    validation_split=0.2
)

train_data = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training",
    shuffle=True,
    seed=42
)

val_data = val_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation",
    shuffle=False
)

num_classes = len(train_data.class_indices)

print("\nDetected classes:")
print(train_data.class_indices)

# =========================
# CLASS WEIGHTS
# =========================

class_weights_array = compute_class_weight(
    class_weight="balanced",
    classes=np.unique(train_data.classes),
    y=train_data.classes
)

class_weights = dict(
    enumerate(class_weights_array)
)

print("\nClass weights:")
print(class_weights)

# =========================
# MOBILE NET V2
# =========================

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)

# Freeze pretrained layers initially
base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)
x = Dropout(0.4)(x)

output = Dense(
    num_classes,
    activation="softmax"
)(x)

model = Model(
    inputs=base_model.input,
    outputs=output
)

# =========================
# INITIAL TRAINING
# =========================

model.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\n======================================")
print("STAGE 1: TRAINING CLASSIFICATION HEAD")
print("======================================")

callbacks = [
    ModelCheckpoint(
        MODEL_SAVE_PATH,
        monitor="val_accuracy",
        save_best_only=True,
        verbose=1
    ),

    EarlyStopping(
        monitor="val_accuracy",
        patience=5,
        restore_best_weights=True,
        verbose=1
    ),

    ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.3,
        patience=2,
        min_lr=1e-7,
        verbose=1
    )
]

history1 = model.fit(
    train_data,
    validation_data=val_data,
    epochs=INITIAL_EPOCHS,
    class_weight=class_weights,
    callbacks=callbacks
)

# =========================
# FINE-TUNING
# =========================

print("\n======================================")
print("STAGE 2: FINE-TUNING MOBILENETV2")
print("======================================")

base_model.trainable = True

# Freeze early layers.
# Fine-tune only the later layers.
for layer in base_model.layers[:-40]:
    layer.trainable = False

# Keep BatchNormalization layers frozen
# for more stable fine-tuning on the small dataset.
for layer in base_model.layers:
    if isinstance(layer, tf.keras.layers.BatchNormalization):
        layer.trainable = False

model.compile(
    optimizer=Adam(learning_rate=1e-5),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

history2 = model.fit(
    train_data,
    validation_data=val_data,
    epochs=FINE_TUNE_EPOCHS,
    class_weight=class_weights,
    callbacks=callbacks
)

# =========================
# FINAL SAVE
# =========================

model.save(MODEL_SAVE_PATH)

print("\n======================================")
print("TRAINING COMPLETE")
print("Model saved as:")
print(MODEL_SAVE_PATH)
print("======================================")
