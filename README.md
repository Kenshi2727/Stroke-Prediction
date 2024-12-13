<h1>Stroke Prediction App</h1>

<h3>Introduction</h3>

This repository houses a machine learning model designed to predict the risk of stroke based on a range of health factors. The model is deployed as a user-friendly web application, enabling individuals to input their health information and receive a risk assessment.

<h3>Getting Started</h3>

<h3>Prerequisites:</h3>
<b>Python</b>: Ensure you have Python installed.

<b>Required Libraries</b>: Install the necessary libraries using the following command:

<b>Bash</b>

pip install -r requirements.txt
Running the Web App:
Start the Server:

<b>Bash</b>

python stroke_prediction_web_app.py
Access the App:
Open your web browser and navigate to http://127.0.0.1:5000.
<b>
Data
</b>
The dataset.csv file contains the dataset used to train the model. It encompasses various health factors, such as age, gender, hypertension, heart disease, smoking history, and more.
<b>
Model
</b>
dtc_balanced.pkl: This file stores the trained decision tree classifier model.
scaler.pkl: This file contains the scaler used for data preprocessing.
stroke_prediction.ipynb: This notebook outlines the code for training and evaluating the model.
<b>Web App</b>

The stroke_prediction_web_app.py script powers the web application. It provides a user-friendly interface for inputting health information and receiving predictions.

<b>Contributing</b>

We encourage contributions to enhance the model and the web app. Feel free to fork the repository and submit pull requests.

<b>License</b>

This project is licensed under the MIT License. For more details, please refer to the LICENSE file.

<b>Acknowledgements</b>

We express our gratitude to the original dataset providers and the open-source community for their valuable contributions to this project.

<b>Disclaimer</b>

Please note that this app is intended for informational purposes only and should not be considered a substitute for professional medical advice. Always consult with 1  a healthcare professional 2  for any health concerns.


<b>Web App Preview</b>
![image](https://github.com/user-attachments/assets/901e29a8-e0a1-4caa-919e-62be65147977)
![image](https://github.com/user-attachments/assets/b7b5166d-ea70-420e-a578-fad7f03d9a2e)
![image](https://github.com/user-attachments/assets/f16f0389-1c5a-4275-a2a3-a465512c486c)
![image](https://github.com/user-attachments/assets/50c831eb-6034-44ab-925b-74864b42ab24)
![image](https://github.com/user-attachments/assets/1cf55fdb-d170-4e78-a8cd-deef13224457)




