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

# Custom Styles
st.markdown("""
    <style>
        .title { text-align: center; font-size: 40px; color: #FF4B4B; }
        .subheader { text-align: center; font-size: 20px; color: #333333; }
        .footer { text-align: center; font-size: 16px; color: gray; margin-top: 20px; }
        .section-header { font-size: 18px; color: #007BFF; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# Title and Intro
st.markdown("<p class='title'>🧠 Stroke Prediction App</p>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>A tool to predict stroke risk based on health indicators.</p>", unsafe_allow_html=True)

st.image(os.path.join(working_dir, 'Stroke.webp'), use_column_width=True)

st.write("Please provide the following details to predict your stroke risk:")

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

# Radar Chart Data Preparation
chart_data = {
    "labels": ["Age", "Hypertension", "Heart Disease", "BMI", "Glucose Level"],
    "values": [age, 1 if hypertension == "Yes" else 0, 1 if heart_disease == "Yes" else 0, bmi, glucose_level]
}

# Radar Chart using Chart.js
st.markdown("---")
st.subheader("📊 Health Indicator Analysis")

st.components.v1.html(f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div style="width: 100%; max-width: 600px; margin: auto;">
        <canvas id="radarChart"></canvas>
    </div>
    <script>
        const ctx = document.getElementById('radarChart').getContext('2d');
        new Chart(ctx, {{
            type: 'radar',
            data: {{
                labels: {chart_data["labels"]},
                datasets: [{{
                    label: 'Health Indicators',
                    data: {chart_data["values"]},
                    fill: true,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    pointBackgroundColor: 'rgba(54, 162, 235, 1)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgba(54, 162, 235, 1)'
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{
                        display: true,
                        position: 'top'
                    }}
                }},
                scales: {{
                    r: {{
                        angleLines: {{
                            display: true
                        }},
                        suggestedMin: 0,
                        suggestedMax: 100
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
""", height=500)

# Footer
st.markdown("---")
st.markdown("""
<p class='footer'>
    Developed with ❤️ by <b>Ashutosh Tiwari</b>  
    [LinkedIn](https://www.linkedin.com/in/ashutosh-tiwari-84a09127b/) | [GitHub](https://github.com/AshutoshTiwari0)
</p>
""", unsafe_allow_html=True)
