import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# -------------------------------
# Model Configuration
# -------------------------------
MODEL_PATH = "mobilenetv2_crop_disease.h5"

# Check if model exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model file '{MODEL_PATH}' not found. "
        "Please place it in the project folder."
    )

# Load the trained model
model = load_model(MODEL_PATH)

# Class labels (must match training order)
class_names = [
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

# Symptoms dictionary
symptoms = {
    "Citrus_Healthy": "No visible symptoms",
    "Citrus_Unhealthy": "Yellowing leaves, black spots",
    "Potato_Healthy": "No visible symptoms",
    "Potato_Unhealthy": "Dark lesions on leaves and stems",
    "Rice_Healthy": "No visible symptoms",
    "Rice_Unhealthy": "Leaf blight, yellow-orange stripes",
    "Tomato_Healthy": "No visible symptoms",
    "Tomato_Unhealthy": "Leaf curl, dark spots, wilting",
    "Wheat_Healthy": "No visible symptoms",
    "Wheat_Unhealthy": "Rust spots, discolored patches",
}


def preprocess_frame(frame):
    """
    Resize and preprocess image for MobileNetV2.
    """
    img = cv2.resize(frame, (224, 224))
    img = img.astype(np.float32)
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img


def predict_crop(frame):
    """
    Predict crop health from a frame.
    Returns crop name, health status, confidence, and symptoms.
    """
    processed = preprocess_frame(frame)

    prediction = model.predict(processed, verbose=0)

    class_index = np.argmax(prediction[0])
    confidence = float(prediction[0][class_index])

    label = class_names[class_index]
    crop_name, health_status = label.split("_")

    symptom_text = symptoms.get(label, "Unknown")

    return crop_name, health_status, confidence, symptom_text


def main():
    # Open webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access webcam.")
        return

    print("Crop Health Detector Started")
    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame.")
            break

        # Mirror image
        frame = cv2.flip(frame, 1)

        # Prediction
        crop_name, health_status, confidence, symptom_text = predict_crop(frame)

        color = (0, 255, 0) if health_status == "Healthy" else (0, 0, 255)

        cv2.putText(
            frame,
            f"{crop_name}: {health_status}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2,
        )

        cv2.putText(
            frame,
            f"Confidence: {confidence * 100:.2f}%",
            (10, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2,
        )

        cv2.putText(
            frame,
            f"Symptoms: {symptom_text}",
            (10, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2,
        )

        cv2.imshow("Crop Health Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()