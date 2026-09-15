import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import os

model = load_model("mobilenetv2_crop_disease.h5")

class_names = [
    "Citrus_Diseased", "Citrus_Healthy", "Citrus_Symptomised",
    "Potato_Diseased", "Potato_Healthy", "Potato_Symptomised",
    "Rice_Diseased", "Rice_Healthy", "Rice_Symptomised",
    "Tomato_Diseased", "Tomato_Healthy", "Tomato_Symptomised",
    "Wheat_Diseased", "Wheat_Healthy", "Wheat_Symptomised"
]

def predict_image(img):
    img = cv2.resize(img, (224, 224))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_array = np.expand_dims(img_rgb, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array, verbose=0)[0]

    max_index = np.argmax(predictions)
    confidence = float(predictions[max_index])

    predicted_label = class_names[max_index]
    crop, condition = predicted_label.split("_", 1)

    if condition == "Healthy":
        message = f"{crop} is Healthy"
    elif condition == "Symptomised":
        message = f"{crop} shows Symptoms"
    else:
        message = f"{crop} is Diseased"

    return message, predicted_label, confidence


image_path = input("Enter path to plant image: ").strip().strip('"')

if not os.path.exists(image_path):
    print("Image path does not exist.")
else:
    img = cv2.imread(image_path)

    if img is None:
        print("Unable to read the image.")
    else:
        result, label, confidence = predict_image(img)

        print()
        print("Prediction:", result)
        print("Class:", label)
        print(f"Confidence: {confidence * 100:.2f}%")

        cv2.putText(
            img,
            f"{label} ({confidence * 100:.1f}%)",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.imshow("Crop Disease Prediction", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()