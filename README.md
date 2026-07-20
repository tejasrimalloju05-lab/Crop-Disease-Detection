# 🌿 Crop Disease Detection using MobileNetV2

## 📌 Overview

This project is an AI-powered Crop Disease Detection system that uses the **MobileNetV2** deep learning model to identify whether a crop leaf is healthy or unhealthy through real-time webcam input. The application leverages **TensorFlow**, **OpenCV**, and **NumPy** to preprocess images, perform classification, and display predictions with confidence scores and disease symptoms.

---

## 🚀 Features

- Real-time crop disease detection using a webcam
- MobileNetV2 deep learning model
- Detects healthy and unhealthy crop leaves
- Displays prediction confidence
- Shows symptoms of detected diseases
- Fast image preprocessing and prediction
- Simple and user-friendly interface

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- MobileNetV2

---

## 📂 Project Structure

```
Crop-Disease-Detection/
│── app.py
│── requirements.txt
│── .gitignore
│── README.md
```

---

## 📋 Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/tejasrimalloju05-lab/Crop-Disease-Detection.git
```

2. Move into the project folder.

```bash
cd Crop-Disease-Detection
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Ensure the trained model file (`mobilenetv2_crop_disease.h5`) is available in the project directory before running the application.

5. Run the application.

```bash
python app.py
```

---

## 🌱 Supported Crop Categories

- Citrus
- Potato
- Rice
- Tomato
- Wheat

Each crop is classified as:

- Healthy
- Unhealthy

---

## 📌 Future Improvements

- Support additional crop species
- Detect specific plant diseases
- Improve model accuracy with larger datasets
- Deploy as a web application using Streamlit or Flask
- Mobile application integration

---

## 👩‍💻 Author

**Tejasri Malloju**

If you found this project useful, consider giving it a ⭐ on GitHub.