# -*- coding: utf-8 -*-
"""Distillation Web App.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AEYcNcI4fQO80bGzfTqC7T0BcWfG8RlH
"""

!pip install joblib
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('/content/rf_trained_model.joblib')

# Define the prediction function
def predict(model, input_data):
    # Make predictions using the loaded model
    predictions = model.predict(input_data)

    return predictions[0]

def main():
    # Set the title and description of the app
    st.title('Distillation Dataset Prediction')
    st.write('Enter the input features and get predictions for distillation.')

    # Input form for user to input the features
    input_features = {}  # Create a dictionary to store user input

    st.write("Enter the values for the following features:")

    input_features['Temp1'] = st.number_input('Temp1', value=121)
    input_features['FlowC1'] = st.number_input('FlowC1', value=470)
    input_features['Temp2'] = st.number_input('Temp2', value=374)
    input_features['TempC1'] = st.number_input('TempC1', value=82)
    input_features['Temp3'] = st.number_input('Temp3', value=493)
    input_features['TempC2'] = st.number_input('TempC2', value=491)
    input_features['TempC3'] = st.number_input('TempC3', value=169)
    input_features['Temp4'] = st.number_input('Temp4', value=176)
    input_features['PressureC1'] = st.number_input('PressureC1', value=204)
    input_features['Temp5'] = st.number_input('Temp5', value=493)
    input_features['Temp6'] = st.number_input('Temp6', value=491)
    input_features['OC1'] = st.number_input('OC1', value=4.59)
    input_features['Temp7'] = st.number_input('Temp7', value=1081)
    input_features['Temp8'] = st.number_input('Temp8', value=521)
    input_features['TempC9'] = st.number_input('TempC9', value=93)
    input_features['FlowC2'] = st.number_input('FlowC2', value=71)
    input_features['Temp9'] = st.number_input('Temp9', value=463)
    input_features['Temp10'] = st.number_input('Temp10', value=514)
    input_features['FlowC3'] = st.number_input('FlowC3', value=8.45)
    input_features['FlowC4'] = st.number_input('FlowC4', value=10.43)
    input_features['Temp11'] = st.number_input('Temp11', value=29.84)
    input_features['Temp12'] = st.number_input('Temp12', value=492)
    input_features['InvTemp1'] = st.number_input('InvTemp1', value=2.03)
    input_features['InvTemp2'] = st.number_input('InvTemp2', value=2.67)
    input_features['InvTemp3'] = st.number_input('InvTemp3', value=2.15)
    input_features['InvPressure1'] = st.number_input('InvPressure1', value=4.57)

    # Convert the user input to a DataFrame
    input_df = pd.DataFrame([input_features])

    if st.button('Predict'):  # Trigger the prediction when the user clicks the "Predict" button
        prediction = predict(model, input_df)  # Call the predict function
        st.write(f'Predicted distillation value: {prediction}')  # Display the prediction result

if __name__ == '__main__':
    main()