# 🌱 Plant Health Monitoring System

[![Streamlit App](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Supabase](https://img.shields.io/badge/Powered%20by-Supabase-3ecf8e.svg)](https://supabase.com)

A deep learning-powered app to monitor plant health and classify leaf diseases using computer vision. Built with **Streamlit** for interactive UI, **TensorFlow** for image classification, and **Supabase** for authentication.

---


## 🚀 Features

- 🔐 User login & registration with Supabase
- 🌿 Upload and classify plant leaf images
- 🤖 CNN-based disease prediction with TensorFlow
- 🎨 Dark-mode UI with custom styling (CSS-in-Streamlit)
- 📊 Extendable for live sensor data and environmental metrics

---

## 🧠 Model Overview

This app uses a Convolutional Neural Network (CNN) trained on a dataset of plant leaf images.

**Training Details:**

- 📁 Dataset: [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease) (38 classes of healthy & diseased leaves)
- 🏗️ Model Architecture:
  - `Conv2D` layers with ReLU activation
  - `MaxPooling2D`
  - `Dropout` for regularization
  - `Dense` fully connected layers
  - `Softmax` for classification
- 📐 Input Size: `224x224x3`
- 📊 Optimizer: `Adam`
- 🧪 Loss: `categorical_crossentropy`
- 🎯 Accuracy: >95% on validation set

> You can retrain your model using the provided notebook: `Plant_Disease_Prediction_CNN_Image_Classifier.ipynb`

---

## 📁 Project Structure
<pre> 
📁 Plant-Health-Monitoring/
├── 📄 main.py                                  # 🚀 Streamlit app (UI + Supabase + ML inference)
│
├── 📁 trained_model/                           # 🤖 Pretrained model assets
│   ├── 📄 plant_disease_prediction_model.h5     # Trained CNN model (Keras/TensorFlow)
│   └── 📄 class_indices.json                    # Mapping of class indices to disease labels
│
├── 📁 Plant-Disease-Prediction-CNN-Image-Classifier-Model/
│   ├── 📄 Plant_Disease_Prediction_CNN_Image_Classifier.ipynb  # 📓 Jupyter Notebook for model training
│   └── 📄 Plant_Disease_Prediction_CNN_Image_Classifier.pdf
├── 📁 Test_Iamge/
│   ├── 🖼️ test_apple_black_rot (1).JPG
│   ├── 🖼️ test_blueberry_healthy.jpg
│   └── 🖼️ test_potato_early_blight.jpg
└── 📄 README.md                                # 📘 Project documentation
 
</pre>

---

## 🛠️ Tech Stack

| Tool         | Role                              |
|--------------|-----------------------------------|
| Streamlit    | Web app frontend & backend        |
| TensorFlow   | Model inference engine            |
| Supabase     | Authentication & session handling |
| PIL / NumPy  | Image preprocessing               |
| Pandas       | Data handling (optional/expandable) |
| Matplotlib & Seaborn | Data visualization (optional) |

---

## 🧪 How It Works

1. Users sign in or register via Supabase.
2. Navigate to **Plant Disease Classifier** and upload a leaf image.
3. The image is resized, normalized, and passed to a deep learning model.
4. The app displays the predicted disease class from the model output.

---

## ⚙️ Installation

 1. Clone the repository
    ```bash
    git clone https://github.com/LakshTrivedi/Plant-Health-Monitoring.git
    cd Plant-Health-Monitoring
2. Create & activate a virtual environment
   ```bash
    python -m venv venv
    # Activate on Mac/Linux
    source venv/bin/activate
    # Activate on Windows
    venv\Scripts\activate
3. Install dependencies
    ```bash
    pip install Streamlit TensorFlow Supabase PIL NumPy Pandas Matplotlib Seaborn
4. Run the Streamlit app
    ```bash
    streamlit run main.py
  Then visit: http://localhost:8501

---

## 🔐 Environment Setup
Set your Supabase credentials in `main.py`:

      API_URL = "your-supabase-url"
      API_KEY = "your-supabase-api-key"

---

## 📊 Model Info
The app uses a pre-trained TensorFlow model for plant disease classification. You can retrain your own model and replace `plant_disease_prediction_model.h5` and `class_indices.json` in the `trained_model/` directory.

---

## 📸 Live Demo

![image](https://github.com/user-attachments/assets/9d8cc3ec-61f2-4a32-b83e-2d83f00b4811)
![image](https://github.com/user-attachments/assets/0502bc0a-a2f3-41c1-addc-d1bc8ca849ba)
![image](https://github.com/user-attachments/assets/93fdc440-72c0-4e92-91ff-f3cec0e9c28d)

---

## 🧑‍💻 Collaborators

| Name           | Enrollment Number      | Role                 |
|----------------|------------------------|-----------------------|
| Mehul Labana   | `KU2407U419`           | ML Model Trainer          |
| Laksh Trivedi  | `KU2407U420`           | Project Lead & Developer |
| Namra Patel    | `KU2407U428`           | Backend Developer        |
---

## 🤝 Connect With US

Mehul Labana&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/PHOENIX24M)&nbsp;&nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mehul-labana-3aa301320?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

Laksh Trivedi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/LakshTrivedi)&nbsp;&nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/laksh-trivedi-87a6a6327/)

Namra Patel&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NamraPatel21)&nbsp;&nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/namra-patel-8a5a3b329?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)
