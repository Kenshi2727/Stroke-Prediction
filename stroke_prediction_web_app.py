import streamlit as st
import os

# Page Configurations
st.set_page_config(
    page_title="Stroke Prediction App",
    page_icon="🧠",
    layout="centered"
)

# Title
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🧠 Stroke Prediction App</h1>", unsafe_allow_html=True)
st.write("This tool predicts stroke risk and visualizes your health indicators.")

# Inputs for the Bar Chart
st.sidebar.header("Input Your Health Indicators")
age = st.sidebar.number_input("Age", min_value=1, step=1, value=25)
hypertension = st.sidebar.radio("Hypertension", ["Yes", "No"])
heart_disease = st.sidebar.radio("Heart Disease", ["Yes", "No"])
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

# Embed the Bar Chart using Chart.js
st.subheader("📊 Health Indicator Bar Chart")
st.components.v1.html(f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div style="width: 100%; max-width: 600px; margin: auto;">
        <canvas id="myBarChart"></canvas>
    </div>
    <script>
        var ctx = document.getElementById('myBarChart').getContext('2d');
        new Chart(ctx, {{
            type: 'bar',
            data: {{
                labels: {chart_data["labels"]},
                datasets: [{{
                    label: 'Health Indicators',
                    data: {chart_data["values"]},
                    backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 
                                      'rgba(255, 206, 86, 0.6)', 'rgba(75, 192, 192, 0.6)', 
                                      'rgba(153, 102, 255, 0.6)'],
                    borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 
                                  'rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)', 
                                  'rgba(153, 102, 255, 1)'],
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                scales: {{
                    y: {{
                        beginAtZero: true
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
""", height=500)
