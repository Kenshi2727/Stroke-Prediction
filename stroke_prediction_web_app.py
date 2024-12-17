import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

# Set Page Config
st.set_page_config(page_title="Dynamic Stroke Prediction", page_icon="⚡", layout="centered")

# Custom CSS for styling and animations
st.markdown("""
    <style>
    /* Background Animation */
    body {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #ffdde1);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Poppins', sans-serif;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Title Animation */
    .title {
        text-align: center;
        font-size: 3rem;
        color: #fff;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
        animation: flicker 1.5s infinite alternate;
    }
    @keyframes flicker {
        0% { text-shadow: 2px 2px 5px #fff, 0 0 10px #ff9a9e, 0 0 15px #ffdde1; }
        100% { text-shadow: 2px 2px 10px #fff, 0 0 20px #fad0c4, 0 0 30px #ff9a9e; }
    }

    /* Input Box Styling */
    .stTextInput, .stNumberInput, .stRadio, .stSelectbox {
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        border-radius: 8px;
        margin: 10px 0;
    }

    /* Hover Effect on Buttons */
    .stButton>button {
        background-color: #ff9a9e;
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 8px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 8px 20px rgba(255, 154, 158, 0.5);
    }

    /* Result Styling with Glow */
    .result {
        text-align: center;
        font-size: 1.5rem;
        color: white;
        background-color: rgba(255, 154, 158, 0.8);
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(255, 154, 158, 0.7);
        padding: 15px;
        margin-top: 20px;
        animation: glow 2s ease-in-out infinite alternate;
    }

    @keyframes glow {
        0% { box-shadow: 0 0 15px rgba(255, 154, 158, 0.7); }
        100% { box-shadow: 0 0 30px rgba(250, 208, 196, 0.8); }
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 0.9rem;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.markdown("<p class='title'>⚡ Stroke Prediction System ⚡</p>", unsafe_allow_html=True)
st.write("Enter your details below to predict your risk of a stroke.")

# Inputs
st.subheader("Personal Information")
gender = st.radio("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, step=1)

st.subheader("Health Details")
hypertension = st.radio("Do you suffer from Hypertension?", ["Yes", "No"])
heart_disease = st.radio("Do you suffer from Heart Disease?", ["Yes", "No"])

st.subheader("Lifestyle")
ever_married = st.radio("Marital Status", ["Yes", "No"])
work_type = st.selectbox("Work Type", ["Children", "Private", "Never worked", "Self-employed", "Govt_job"])
residence_type = st.radio("Residence Type", ["Rural", "Urban"])
glucose_level = st.number_input("Average Glucose Level", min_value=0.1, format="%.2f")
bmi = st.number_input("Body Mass Index", min_value=0.1, format="%.2f")

smoking_status = st.selectbox("Smoking Status", ["Yes", "No", "Occasionally"])

# Mapping Smoking Status
smoking_mapping = {"Yes": "smokes", "No": "never smoked", "Occasionally": "formerly smoked"}
mapped_smoking_status = smoking_mapping[smoking_status]

# Preprocess Input
working_dir = os.path.dirname(os.path.abspath(__file__))
scaler_path = os.path.join(working_dir, 'scaler.pkl')
model_path = os.path.join(working_dir, 'dtc_balanced.pkl')

# Load Model and Scaler
with open(scaler_path, "rb") as scaler_file:
    scaler = pickle.load(scaler_file)
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

scaled_age = scaler.fit_transform([[age]])[0][0]
glucose_level = np.log(glucose_level) if glucose_level > 0 else 0
bmi = np.log(bmi) if bmi > 0 else 0

input_data = pd.DataFrame([{
    "gender": gender, "age": scaled_age, "hypertension": hypertension, "heart_disease": heart_disease,
    "ever_married": ever_married, "work_type": work_type, "Residence_type": residence_type,
    "avg_glucose_level": glucose_level, "bmi": bmi, "smoking_status": mapped_smoking_status
}])

# Prediction
prediction = model.predict(input_data)

# Display Result
st.markdown("---")
st.subheader("Your Stroke Prediction Result:")
if prediction[0] == 1:
    st.markdown("<div class='result'>⚠️ You are at risk of having a stroke. Please consult a healthcare professional!</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='result'>✅ You are not at risk of a stroke. Keep maintaining a healthy lifestyle!</div>", unsafe_allow_html=True)

# Footer
st.markdown("<p class='footer'>✨ Built with ❤️ by Ashutosh Tiwari | [LinkedIn](https://www.linkedin.com/in/ashutosh-tiwari-84a09127b/) | [GitHub](https://github.com/AshutoshTiwari0)</p>", unsafe_allow_html=True)
