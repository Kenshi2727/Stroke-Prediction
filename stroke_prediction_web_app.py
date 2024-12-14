import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import os


# Get the directory of the current script
working_dir = os.path.dirname(os.path.abspath(__file__))


st.write("Stroke Prediction")
st.write("A stroke occurs when blood flow to the brain is interrupted or reduced, depriving brain cells of oxygen and nutrients. This can lead to severe health complications, disability, or even death if not treated promptly.")

image_path = os.path.join(working_dir, 'Stroke.webp')
st.image(image_path)

st.write("Please enter the following data")

#getting the input features

#gender feature
gender=st.radio("Enter Your Gender",
                ["Male","Female"])

#age feature
age=st.number_input("Enter Your Age",min_value=0)


#Hyper Tension feature
hypertension=st.radio("Do You Suffer From Hyper Tension?",
                         ["Yes","No"])


#Heart Disease feature
heart_disease=st.radio("Do You Suffer From Heart Disease?",
                         ["Yes","No"])



#married feature
ever_married=st.radio("What's Your Maritial Status?",
                         ["Yes","No"])

#work_type Feature
work_type=st.radio("What's Your Work Type?",
                   ["children","Private","Never_worked","Self-employed","Govt_job"])


#Residence_type Feature
residence_type=st.radio("What's Your Residence Type?",
                   ["Rural","Urban"])

#glucose_avg_level feature (log transformed hai bhai yaad rkhiyo)
glucose_level=st.number_input("What's Your Average Glucose Level?")

#bmi feature (log transformed hai bhai yaad rkhiyo)
bmi=st.number_input("What's Your Body Mass Index?")

#smoking_status feature
smoking_status=st.selectbox("Do You Smoke?",
                            ["Yes","No","Occasionally"])

smoking_status_mapping = {
    "Yes": "smokes",           # "Yes" corresponds to "smokes"
    "No": "never smoked",      # "No" corresponds to "never smoked"
    "Occasionally": "formerly smoked"  # "Occasionally" corresponds to "formerly smoked"
}

# Build paths relative to the working directory
scaler_path = os.path.join(working_dir, 'scaler.pkl')
model_path = os.path.join(working_dir, 'dtc_balanced.pkl')


mapped_smoking_status = smoking_status_mapping[smoking_status]

# Load the scaler
with open(scaler_path, "rb") as scaler_file:
     scaler = pickle.load(scaler_file)

#scaling the age
scaled_age=scaler.fit_transform([[age]])[0][0]


input_data = {
    'gender': gender,
    'age': scaled_age,
    'hypertension': hypertension,  # Ensure the column name matches exactly
    'heart_disease': heart_disease,
    'ever_married': ever_married,  # Corrected column name
    'work_type': work_type,
    'Residence_type': residence_type,
     'avg_glucose_level': glucose_level,  # Ensure this column name matches exactly
      'bmi': bmi, # Ensure this column name matches exactly
    'smoking_status': mapped_smoking_status
}
   
# Check if the value of glucose is valid (positive)
if glucose_level <= 0:
    st.warning("Please provide a valid value for average glucose level (must be greater than 0).")
else:
    # Proceed with scaling and prediction
    glucose_level = np.log(glucose_level)  # If log-transformed earlier
    
if bmi <= 0:
    st.warning("Please provide a valid value for BMI (must be greater than 0).")
else:
    bmi = np.log(bmi)

# Label encoding handling
encode = ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']

# Initialize LabelEncoder
le = LabelEncoder()

# Label encode all the categorical features in the 'encode' list
for feature in encode:
    input_data[feature] = le.fit_transform([input_data[feature]])[0]  # Encoding the feature

# Update log-transformed features
input_data['avg_glucose_level'] = glucose_level
input_data['bmi'] = bmi


#convert input data to dataframe
input_df=pd.DataFrame([input_data])


#working_dir=os.path.dirname(os.path.abspath(__file__))
#try:
#    with open(os.path.join(working_dir,'Model/dtc_balanced.pkl'),'rb') as file:
#        model=pickle.load(file)
#except FileNotFoundError:
#    st.error("file not found")

# Load the model
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)
# Make prediction
prediction = model.predict(input_df)



# Display the prediction result
if prediction == 1:
    st.write("You are at risk of having a stroke.")
else:
    st.write("You are not at risk of having a stroke.")

st.write("### Stroke Prevention Guidelines")

st.markdown("""
1. **Blood Pressure**:  
   - Manage blood pressure with medication.  
   - Most patients need to take at least two antihypertensive medications to reach their goal.

2. **Physical Activity**:  
   - Get at least 30 minutes of moderate physical activity most days of the week.  
   - Healthy adults should aim for at least 40 minutes of moderate- to vigorous-intensity aerobic physical activity 3 to 4 days a week.

3. **Diet**:  
   - Choose healthy foods and drinks.

4. **Weight**:  
   - Maintain a healthy weight.

5. **Smoking**:  
   - Don't smoke.

6. **Alcohol**:  
   - Limit alcohol consumption.

7. **Medical Conditions**:  
   - Control medical conditions like diabetes and heart disease.

8. **Cholesterol**:  
   - Check and manage cholesterol levels.

9. **Pregnancy**:  
   - Manage hypertension during pregnancy and within 6 weeks postpartum.

10. **Antiplatelet Therapy**:  
    - Take antiplatelet therapy if you have antiphospholipid syndrome or systemic lupus erythematosus without a history of stroke.

11. **Vitamin K Antagonist Therapy**:  
    - Take vitamin K antagonist therapy if you have antiphospholipid syndrome and a prior unprovoked venous thrombosis.
""")


# Footer
st.markdown("---")
st.markdown("**Built by Ashutosh Tiwari**")  
st.markdown("Connect with me on [LinkedIn](https://www.linkedin.com/in/ashutosh-tiwari-84a09127b/) or [GitHub](https://github.com/AshutoshTiwari0).")

