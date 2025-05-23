import os
import json
from PIL import Image
import numpy as np
import tensorflow as tf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from supabase import create_client

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# ---------------------
# Setup
# ---------------------
API_KEY = 
API_URL = 
supabase = create_client(API_URL, API_KEY)

st.set_page_config(page_title="Plant Health Monitoring", layout='wide')

# ---------------------
# Session
# ---------------------
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'user' not in st.session_state:
    st.session_state['user'] = None

# ---------------------
# Custom Styles
# ---------------------
st.markdown("""
    <style>
        .stApp {
            background-color: #000000;
            color: #1DCD9F;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-header {
            background-color: #169976;
            color: white;
            padding: 1rem;
            text-align: center;
            font-size: 28px;
            border-radius: 5px;
        }
        .stSidebar > div:first-child {
            background-color: #222222;
        }
        .css-10trblm, .css-1v3fvcr, .css-qrbaxs {
            color: #1DCD9F !important;
        }
        .stTextInput > div > div > input,
        .stTextInput > div > div > textarea {
            background-color: #222222 !important;
            color: #1DCD9F !important;
            border: 1px solid #1DCD9F !important;
        }
        .stButton > button {
            background-color: #1DCD9F !important;
            color: #000000 !important;
            border: none !important;
        }
        .stButton > button:hover {
            background-color: #169976 !important;
            color: white !important;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #1DCD9F !important;
        }
        .stSuccess, .stWarning, .stError {
            background-color: #222222 !important;
            border-color: #1DCD9F !important;
            color: #1DCD9F !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🌱 Plant Health Monitoring System</div>', unsafe_allow_html=True)

# ---------------------
# Navigation
# ---------------------
if st.session_state['authenticated']:
    nav_selection = st.sidebar.radio("Navigation", ["Home", "Plant Disease Classifier", "Logout"])
else:
    nav_selection = st.sidebar.radio("Navigation", ["Home", "Login", "Register"])

# ---------------------
# Home Page
# ---------------------
if nav_selection == "Home":
    st.title("Welcome to the Plant Health Monitoring Dashboard")
    st.markdown("""
        Stay on top of your garden's health with real-time sensor data and intelligent plant disease prediction powered by AI.
    """)

# ---------------------
# Register Page
# ---------------------
elif nav_selection == "Register":
    st.title("👤 Register")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        try:
            res = supabase.auth.sign_up({"email": email, "password": password})
            if res.user:
                st.success("Registered successfully! Please verify your email.")
            else:
                st.error("Registration failed.")
        except Exception as e:
            st.error(f"Error: {e}")

# ---------------------
# Login Page
# ---------------------
elif nav_selection == "Login":
    st.title("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            res = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if res.user:
                st.session_state['authenticated'] = True
                st.session_state['user'] = res.user
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Login failed.")
        except Exception as e:
            st.error(f"Error: {e}")

# ---------------------
# Logout
# ---------------------
elif nav_selection == "Logout":
    supabase.auth.sign_out()
    st.session_state['authenticated'] = False
    st.session_state['user'] = None
    st.success("Logged out successfully.")
    st.rerun()

# ---------------------
# Plant Disease Classifier
# ---------------------
elif nav_selection == "Plant Disease Classifier" and st.session_state['authenticated']:
    st.title("🌿 Plant Disease Classifier")
    working_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = f"{working_dir}/trained_model/plant_disease_prediction_model.h5"
    model = tf.keras.models.load_model(model_path)
    class_indices = json.load(open(f"{working_dir}/trained_model/class_indices.json"))

    def load_and_preprocess_image(image_path, target_size=(224, 224)):
        img = Image.open(image_path)
        img = img.resize(target_size)
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array.astype('float32') / 255.
        return img_array

    def predict_image_class(model, image_path, class_indices):
        preprocessed_img = load_and_preprocess_image(image_path)
        predictions = model.predict(preprocessed_img)
        predicted_class_index = np.argmax(predictions, axis=1)[0]
        return class_indices[str(predicted_class_index)]

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=200)
        if st.button("Classify"):
            prediction = predict_image_class(model, uploaded_image, class_indices)
            st.success(f"Prediction: {prediction}")
