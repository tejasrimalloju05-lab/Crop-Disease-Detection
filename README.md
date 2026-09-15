# 🌿 Crop Health Detection using MobileNetV2

## 📌 Overview

Crop diseases and unhealthy plant conditions can significantly affect agricultural productivity and crop quality. This project uses **Deep Learning and Transfer Learning with MobileNetV2** to classify crop leaf images into **Healthy** and **Unhealthy** categories.

The system processes a crop leaf image using computer vision techniques and predicts the **crop type, health condition, and prediction confidence**.

The project supports five crop categories:

* Citrus
* Potato
* Rice
* Tomato
* Wheat

Each crop is classified as either **Healthy or Unhealthy**, resulting in **10 output classes**.

> **Note:** This project performs crop health classification. It does not identify a specific disease name.

---

## 🎯 Objectives

* Detect whether a crop leaf appears healthy or unhealthy.
* Classify the crop into its respective category.
* Use MobileNetV2 and transfer learning for image classification.
* Display prediction confidence.
* Perform image preprocessing using OpenCV and NumPy.
* Support real-time webcam-based prediction.
* Provide a lightweight computer-vision-based crop health detection system.

---

## 🚀 Features

* 🌱 Crop health classification
* 📷 Image-based prediction
* 🎥 Real-time webcam prediction
* 🧠 MobileNetV2 deep learning model
* 📊 Prediction confidence score
* 🌿 Support for 5 crop categories
* 🩺 Basic symptom information for unhealthy classifications
* ⚡ Image preprocessing and real-time prediction
* 💻 Python-based computer vision application

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

The project uses **MobileNetV2**, a lightweight convolutional neural network architecture designed for efficient image classification.

Transfer learning is used to adapt the pretrained MobileNetV2 architecture for crop leaf health classification.

### Image Processing Pipeline

```text
Input Crop Leaf Image
        ↓
Image Preprocessing
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

For webcam prediction, frames are captured using OpenCV and processed through the same prediction pipeline.

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
├── dataset/
│
├── clean_dataset/
├── training_dataset/
│
├── predict_image.py
├── real_time_webcam_prediction.py
│
├── train_model.py
├── preprocess_images.py
│
├── analyze_dataset.py
├── analyze_clean_dataset.py
├── check_images.py
├── check_duplicates.py
├── clean_duplicates.py
│
├── mobilenetv2_crop_disease.h5
├── requirements.txt
├── .gitignore
└── README.md
```

> The trained model file may be excluded from the GitHub repository because of file-size limitations. If it is not included, place the required model file in the project root before running the prediction scripts.

---

## 📋 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tejasrimalloju05-lab/Crop-Disease-Detection.git
```

### 2. Navigate to the Project Directory

```bash
cd Crop-Disease-Detection
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 1. Image Prediction

Make sure the trained model file is available in the project root:

```text
mobilenetv2_crop_disease.h5
```

Run:

```bash
python predict_image.py
```

The program will ask for the path of a plant leaf image.

Example:

```text
dataset\Tomato\Healthy\000001.jpg
```

The output includes:

```text
Prediction: Tomato is Healthy
Class: Tomato_Healthy
Confidence: 67.85%
```

The exact prediction and confidence will vary depending on the input image.

---

### 2. Real-Time Webcam Prediction

To use the webcam for real-time crop health prediction, run:

```bash
python real_time_webcam_prediction.py
```

The webcam captures the crop leaf and the model predicts the crop category and health status.

To stop the webcam application, press:

```text
q
```

---

## 📊 Dataset

The project uses crop leaf images from five crop categories:

* Citrus
* Potato
* Rice
* Tomato
* Wheat

The classification task contains two health categories for each crop:

* Healthy
* Unhealthy

Therefore, the model produces **10 output classes**.

The dataset and preprocessing workflow are maintained separately from the trained model.

> The complete dataset is not included in the GitHub repository.

---

## 🔍 Prediction Workflow

The system follows these steps:

1. Input a crop leaf image or capture a frame through the webcam.
2. Read the image using OpenCV.
3. Resize the image to **224 × 224 pixels**.
4. Apply the preprocessing required for MobileNetV2.
5. Pass the processed image to the trained deep learning model.
6. Obtain the predicted class.
7. Determine the crop type and health status.
8. Display the prediction confidence.

Example:

```text
Input Image
     ↓
OpenCV
     ↓
224 × 224 Resize
     ↓
MobileNetV2 Preprocessing
     ↓
Trained Model
     ↓
Prediction
     ↓
Tomato + Healthy
     ↓
Confidence Score
```

---

## ⚠️ Limitations

* The model classifies leaves as **Healthy or Unhealthy** rather than identifying a specific disease.
* Prediction performance depends on image quality, lighting, background, camera angle, and leaf visibility.
* The model may perform differently on real-world field images compared with training images.
* The system is an educational/project prototype and should not be treated as a substitute for professional agricultural diagnosis.
* The trained model may not be included directly in the GitHub repository because of file-size limitations.

---

## 🔮 Future Improvements

* Expand the dataset with more diverse real-world field images.
* Identify specific crop diseases instead of only Healthy/Unhealthy conditions.
* Improve model performance using better data augmentation and fine-tuning.
* Add an image-upload interface.
* Develop a web-based interface for easier use.
* Add detailed disease/symptom information.
* Provide recommended actions for detected unhealthy conditions.
* Deploy the model as a web or mobile application.

---

## 👩‍💻 Author

**Tejasri Malloju**

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
