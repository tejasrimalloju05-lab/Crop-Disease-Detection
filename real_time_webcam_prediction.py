import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load the trained model
model = load_model('mobilenetv2_crop_disease.h5')

# Class labels (make sure this order matches model training)
class_names = [
    'Citrus_Healthy', 'Citrus_Unhealthy',
    'Potato_Healthy', 'Potato_Unhealthy',
    'Rice_Healthy', 'Rice_Unhealthy',
    'Tomato_Healthy', 'Tomato_Unhealthy',
    'Wheat_Healthy', 'Wheat_Unhealthy'
]

# Symptoms dictionary
symptoms = {
    'Citrus_Healthy': 'No visible symptoms',
    'Citrus_Unhealthy': 'Yellowing leaves, black spots',
    'Potato_Healthy': 'No visible symptoms',
    'Potato_Unhealthy': 'Dark lesions on leaves and stems',
    'Rice_Healthy': 'No visible symptoms',
    'Rice_Unhealthy': 'Leaf blight, yellow-orange stripes',
    'Tomato_Healthy': 'No visible symptoms',
    'Tomato_Unhealthy': 'Leaf curl, dark spots, wilting',
    'Wheat_Healthy': 'No visible symptoms',
    'Wheat_Unhealthy': 'Rust spots, discolored patches'
}

# Preprocessing function using correct MobileNetV2 input
def preprocess_frame(frame):
    img = cv2.resize(frame, (224, 224))
    img = preprocess_input(img.astype(np.float32))  # Standard MobileNetV2 preprocessing
    img = np.expand_dims(img, axis=0)
    return img

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    frame = cv2.flip(frame, 1)  # Mirror image for natural viewing

    # Predict crop and health status
    processed = preprocess_frame(frame)
    prediction = model.predict(processed)
    class_index = np.argmax(prediction[0])
    confidence = prediction[0][class_index]

    label = class_names[class_index]
    crop_name, health_status = label.split('_')
    symptom_text = symptoms[label]

    display_text = f"{crop_name}: {health_status} ({confidence:.2f})"
    color = (0, 255, 0) if health_status == 'Healthy' else (0, 0, 255)

    # Display predictions
    cv2.putText(frame, display_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.putText(frame, f"Symptoms: {symptom_text}", (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("Crop Health Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
