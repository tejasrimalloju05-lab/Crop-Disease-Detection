# 🌿 Crop Disease Detection using MobileNetV2

## 📌 Overview

Crop diseases can significantly affect agricultural productivity and crop quality. This project uses **Deep Learning and Transfer Learning with MobileNetV2** to classify crop leaf images into healthy and unhealthy categories.

The system processes an image captured through a webcam, applies image preprocessing, and predicts the crop type and health condition along with a confidence score.

The project supports **five crop categories: Citrus, Potato, Rice, Tomato, and Wheat**, with each crop classified as either **Healthy or Unhealthy**.

> **Note:** This project performs crop health classification and does not identify a specific disease name.

---

## 🎯 Objectives

* Detect whether a crop leaf appears healthy or unhealthy.
* Classify the crop into its respective category.
* Use MobileNetV2 for efficient image classification.
* Display prediction confidence.
* Provide basic symptom information for unhealthy classifications.
* Create a lightweight computer-vision-based crop health detection system.

---

## 🚀 Features

* 🌱 Crop health classification
* 📷 Real-time webcam-based image input
* 🧠 MobileNetV2 deep learning model
* 📊 Prediction confidence score
* 🌿 Support for 5 crop categories
* 🩺 Basic symptom information
* ⚡ Fast image preprocessing and prediction
* 💻 Simple Python-based application

---

## 🌱 Supported Crops

| Crop   | Classification      |
| ------ | ------------------- |
| Citrus | Healthy / Unhealthy |
| Potato | Healthy / Unhealthy |
| Rice   | Healthy / Unhealthy |
| Tomato | Healthy / Unhealthy |
| Wheat  | Healthy / Unhealthy |

**Total output classes: 10**

---

## 🧠 Model

The project uses **MobileNetV2**, a lightweight convolutional neural network architecture suitable for image classification and applications with limited computational resources.

### Image Processing Pipeline

```text
Webcam Input
     ↓
Image Capture
     ↓
Resize to 224 × 224
     ↓
MobileNetV2 Preprocessing
     ↓
Trained MobileNetV2 Model
     ↓
Class Prediction
     ↓
Crop + Health Status + Confidence
```

---

## 🛠️ Technologies Used

* **Python**
* **TensorFlow / Keras**
* **MobileNetV2**
* **OpenCV**
* **NumPy**

---

## 📂 Project Structure

```text
Crop-Disease-Detection/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

> The trained model file is excluded from the repository and must be provided separately to run the application.

---

## 📋 Installation

Clone the repository:

```bash
git clone https://github.com/tejasrimalloju05-lab/Crop-Disease-Detection.git
```

Navigate to the project directory:

```bash
cd Crop-Disease-Detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Before running the application, place the trained model file:

```text
mobilenetv2_crop_disease.h5
```

in the project root directory.

Then run:

```bash
python app.py
```

The application will open the webcam and display:

* Crop name
* Healthy/Unhealthy status
* Prediction confidence
* Basic symptom information

Press **`q`** to close the application.

---

## 📊 Dataset

The project was developed using a crop leaf image dataset covering five crop categories:

* Citrus
* Potato
* Rice
* Tomato
* Wheat

Each category contains healthy and unhealthy leaf images.

**Dataset size:** 488 images

> The dataset is not included in this repository.

---

## ⚠️ Limitations

* The model classifies leaves as **Healthy or Unhealthy** rather than identifying a specific disease.
* Prediction performance depends on image quality, lighting, background, and camera conditions.
* The system should be treated as an educational/project prototype and not as a substitute for professional agricultural diagnosis.
* The trained model is currently not included in the repository.

---

## 🔮 Future Improvements

* Expand the dataset with more diverse field images.
* Identify specific crop diseases instead of only healthy/unhealthy conditions.
* Improve model performance using data augmentation and fine-tuning.
* Add image-upload functionality alongside webcam input.
* Develop a web or mobile interface.
* Provide more detailed disease information and recommended actions.
* Deploy the model for easier access by farmers and agricultural users.

---

## 👩‍💻 Author

**Tejasri Malloju**

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 🔍 Prediction Workflow

The system follows these steps to detect crop health:

1. Capture the crop leaf image through a webcam.
2. Preprocess the image using OpenCV and NumPy.
3. Resize and normalize the image for MobileNetV2.
4. Pass the processed image to the trained deep learning model.
5. Predict the crop health category.
6. Display the predicted class and confidence score.

The trained MobileNetV2 model is used to perform image classification efficiently while maintaining a lightweight architecture suitable for real-time prediction.