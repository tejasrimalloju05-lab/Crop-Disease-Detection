import os

import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model

# ==========================================

# Model Configuration

# ==========================================

MODEL_PATH = "mobilenetv2_crop_disease.h5"

CLASS_NAMES = [
"Citrus_Healthy",
"Citrus_Unhealthy",
"Potato_Healthy",
"Potato_Unhealthy",
"Rice_Healthy",
"Rice_Unhealthy",
"Tomato_Healthy",
"Tomato_Unhealthy",
"Wheat_Healthy",
"Wheat_Unhealthy",
]

# Basic visual indicators associated with unhealthy leaves.

# These are informational only and are not medical/agricultural diagnoses.

INDICATORS = {
"Citrus_Healthy": "No visible abnormality",
"Citrus_Unhealthy": "Yellowing leaves, dark spots",
"Potato_Healthy": "No visible abnormality",
"Potato_Unhealthy": "Dark lesions on leaves",
"Rice_Healthy": "No visible abnormality",
"Rice_Unhealthy": "Leaf discoloration, lesions",
"Tomato_Healthy": "No visible abnormality",
"Tomato_Unhealthy": "Leaf curl, dark spots, wilting",
"Wheat_Healthy": "No visible abnormality",
"Wheat_Unhealthy": "Rust-like spots, discoloration",
}

# ==========================================

# Load Model

# ==========================================

def load_crop_model():
"""Load the trained MobileNetV2 model."""
if not os.path.exists(MODEL_PATH):
raise FileNotFoundError(
f"\nModel file not found: {MODEL_PATH}\n"
"Please place the trained model file in the project directory."
)

```
return load_model(MODEL_PATH)
```

model = load_crop_model()

# ==========================================

# Image Preprocessing

# ==========================================

def preprocess_frame(frame):
"""Resize and preprocess a webcam frame for MobileNetV2."""
image = cv2.resize(frame, (224, 224))
image = image.astype(np.float32)
image = preprocess_input(image)
image = np.expand_dims(image, axis=0)

```
return image
```

# ==========================================

# Prediction

# ==========================================

def predict_crop(frame):
"""
Predict the crop category and health status.

```
Returns:
    crop_name: Predicted crop
    health_status: Healthy or Unhealthy
    confidence: Prediction confidence
    indicator: Informational visual indicator
"""

processed_image = preprocess_frame(frame)

predictions = model.predict(processed_image, verbose=0)

class_index = int(np.argmax(predictions[0]))
confidence = float(predictions[0][class_index])

predicted_label = CLASS_NAMES[class_index]

crop_name, health_status = predicted_label.rsplit("_", 1)

indicator = INDICATORS.get(
    predicted_label,
    "No additional information available"
)

return crop_name, health_status, confidence, indicator
```

# ==========================================

# Main Application

# ==========================================

def main():
"""Start the webcam-based crop health detection system."""

```
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Unable to access the webcam.")
    return

print("==========================================")
print(" Crop Health Detection using MobileNetV2")
print("==========================================")
print("Press 'q' to quit.")

while True:
    success, frame = camera.read()

    if not success:
        print("Error: Failed to capture webcam frame.")
        break

    # Mirror the webcam feed.
    frame = cv2.flip(frame, 1)

    try:
        crop_name, health_status, confidence, indicator = predict_crop(
            frame
        )
    except Exception as error:
        print(f"Prediction error: {error}")
        break

    # Display colors:
    # Green = Healthy
    # Red = Unhealthy
    display_color = (
        (0, 255, 0)
        if health_status == "Healthy"
        else (0, 0, 255)
    )

    cv2.putText(
        frame,
        f"Crop: {crop_name}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        display_color,
        2,
    )

    cv2.putText(
        frame,
        f"Status: {health_status}",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        display_color,
        2,
    )

    cv2.putText(
        frame,
        f"Confidence: {confidence * 100:.2f}%",
        (10, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        display_color,
        2,
    )

    cv2.putText(
        frame,
        f"Indicator: {indicator}",
        (10, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        display_color,
        2,
    )

    cv2.imshow("Crop Health Detector", frame)

    # Press 'q' to exit.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
```

# ==========================================

# Application Entry Point

# ==========================================

if **name** == "**main**":
main()
