import streamlit as st
import os

# Page Configurations
st.set_page_config(
    page_title="Stroke Prediction App",
    page_icon="🧠",
    layout="centered"
)
st.header("Changes kiya hai bhai dekho hua")
# Title
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🧠 Stroke Prediction App</h1>", unsafe_allow_html=True)
st.write("This tool predicts stroke risk and visualizes your health indicators.")

# Inputs for the Polar Chart
st.sidebar.header("Input Your Health Indicators")
age = st.sidebar.number_input("Age", min_value=1, step=1, value=25) #getting age
hypertension = st.sidebar.radio("Hypertension", ["Yes", "No"]) #getting hypertension status
heart_disease = st.sidebar.radio("Heart Disease", ["Yes", "No"]) #getting whether they have heart disease
bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1, value=23.5)
glucose_level = st.sidebar.number_input("Glucose Level", min_value=50.0, max_value=300.0, step=1.0, value=100.0)

# Map Inputs for Chart Data
chart_data = {
    "labels": ["Age", "Hypertension", "Heart Disease", "BMI", "Glucose Level"],
    "values": [
        age,
        1 if hypertension == "Yes" else 0,
        1 if heart_disease == "Yes" else 0,
        bmi,
        glucose_level
    ]
}

# Embed the Polar Chart using Chart.js
st.subheader("📊 Health Indicator Polar Chart")
st.components.v1.html(f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div style="width: 100%; max-width: 600px; margin: auto;">
        <canvas id="myPolarChart"></canvas>
    </div>
    <script>
        var ctx = document.getElementById('myPolarChart').getContext('2d');
        new Chart(ctx, {{
            type: 'polarArea',
            data: {{
                labels: {chart_data["labels"]},
                datasets: [{{
                    label: 'Health Indicators',
                    data: {chart_data["values"]},
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2
                }}]
            }},
            options: {{
                responsive: true,
                scales: {{
                    r: {{
                        beginAtZero: true
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
""", height=500)
