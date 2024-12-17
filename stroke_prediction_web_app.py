import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

# Get working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Page Configurations
st.set_page_config(
    page_title="Stroke Prediction App",
    page_icon="🧠",
    layout="centered"
)

# Custom Styles for Dynamic Background and Elements
st.markdown("""
    <style>
        /* Dynamic Gradient Background */
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1, #ffdde1);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Title and Subheader Styling */
        .title { text-align: center; font-size: 45px; color: #FFFFFF; text-shadow: 2px 2px 4px #333; }
        .subheader { text-align: center; font-size: 20px; color: #222222; }

        /* Stylish Radio Buttons */
        div.stRadio > div { 
            display: flex; justify-content: center; 
            gap: 10px; 
        }
        div.stRadio label span { 
            color: #222; 
            font-weight: bold; 
        }

        /* Section Headers */
        .section-header { font-size: 20px; color: #FF6B6B; margin-top: 20px; text-shadow: 1px 1px 2px #ccc; }

        /* Cards with Shadows */
        .card { 
            background-color: #ffffff;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            margin-top: 10px;
        }

        /* Footer Styling */
        .footer { text-align: center; font-size: 16px; color: #444; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# Title and Intro
st.markdown("<p class='title'>🧠 Stroke Prediction App</p>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>A tool to predict stroke risk based on health indicators.</p>", unsafe_allow_html=True)

# Input Form in a Card
st.markdown("<div class='card'>", unsafe_allow_html=True)

# Input Section
st.markdown("<p class='section-header'>📝 Personal Information</p>", unsafe_allow_html=True)
gender = st.radio("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, step=1)

st.markdown("<p class='section-header'>❤️ Health Details</p>", unsafe_allow_html=True)
hypertension = st.radio("Do you suffer from Hypertension?", ["Yes", "No"])
heart_disease = st.radio("Do you suffer from Heart Disease?", ["Yes", "No"])

st.markdown("<p class='section-header'>🏠 Lifestyle Details</p>", unsafe_allow_html=True)
ever_married = st.radio("Marital Status", ["Yes", "No"])
work_type = st.selectbox("Work Type", ["Children", "Private", "Never_worked", "Self-employed", "Govt_job"])
residence_type = st.radio("Residence Type", ["Rural", "Urban"])

st.markdown("<p class='section-header'>🧪 Health Metrics</p>", unsafe_allow_html=True)
glucose_level = st.number_input("Average Glucose Level", min_value=0.1, format="%.2f")
bmi = st.number_input("Body Mass Index (BMI)", min_value=0.1, format="%.2f")
smoking_status = st.selectbox("Smoking Status", ["Yes", "No", "Occasionally"])

st.markdown("</div>", unsafe_allow_html=True)  # Close Card Div

# Map smoking status
smoking_status_mapping = {
    "Yes": "smokes",
    "No": "never smoked",
    "Occasionally": "formerly smoked"
}
mapped_smoking_status = smoking_status_mapping[smoking_status]

# Load scaler and model
scaler_path = os.path.join(working_dir, 'scaler.pkl')
model_path = os.path.join(working_dir, 'dtc_balanced.pkl')
with open(scaler_path, "rb") as scaler_file:
    scaler = pickle.load(scaler_file)
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

# Preprocess input
scaled_age = scaler.fit_transform([[age]])[0][0]
glucose_level = np.log(glucose_level) if glucose_level > 0 else 0
bmi = np.log(bmi) if bmi > 0 else 0

input_data = {
    'gender': gender, 'age': scaled_age, 'hypertension': hypertension, 'heart_disease': heart_disease,
    'ever_married': ever_married, 'work_type': work_type, 'Residence_type': residence_type,
    'avg_glucose_level': glucose_level, 'bmi': bmi, 'smoking_status': mapped_smoking_status
}

# Encode categorical features
encode = ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
le = LabelEncoder()
for feature in encode:
    input_data[feature] = le.fit_transform([input_data[feature]])[0]

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Prediction
prediction = model.predict(input_df)

# Result with Shadow Card
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<p class='section-header'>🧾 Prediction Result</p>", unsafe_allow_html=True)
if prediction == 1:
    st.error("⚠️ You are at risk of having a stroke. Please consult a healthcare provider.")
else:
    st.success("✅ You are not at risk of having a stroke. Keep maintaining a healthy lifestyle!")
st.markdown("</div>", unsafe_allow_html=True)

# Stroke Prevention Guidelines
with st.expander("💡 **Stroke Prevention Guidelines**", expanded=False):
    st.markdown("""
    1. **Blood Pressure**: Monitor and manage your blood pressure regularly.
    2. **Physical Activity**: Exercise at least 30 minutes a day, 4 times a week.
    3. **Healthy Diet**: Eat a balanced diet rich in fruits and vegetables.
    4. **Weight Management**: Maintain a healthy BMI.
    5. **Smoking Cessation**: Avoid smoking and secondhand smoke.
    6. **Alcohol Consumption**: Limit alcohol intake.
    7. **Manage Conditions**: Treat diabetes, heart disease, and cholesterol levels effectively.
    8. **Medical Therapy**: Take prescribed medications consistently.
    """)

# Footer
st.markdown("<p class='footer'>Developed with ❤️ by <b>Ashutosh Tiwari</b></p>", unsafe_allow_html=True)
