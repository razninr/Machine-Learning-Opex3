# -*- coding: utf-8 -*-
"""Diabetes Web app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tvTvGpl1owYd5ucbguA2AnxHLYNuJnvI
"""

#!pip install streamlit
import numpy as np
import pickle
import streamlit as st

loaded_model= pickle.load(open('C:\Users\RamliR2\OneDrive - BASF\Documents\Azure ML Cheatsheet\trained_model .sav', 'rb'))

def diabetes_prediction(input_data):

  input_data_as_numpy_array = np.asarray(input_data)

# Define the input data
input_data = [6, 148, 72, 35, 0, 33.6, 0.627, 50]

# Reshape the input data
input_data_reshaped = np.array(input_data).reshape(1, -1)

# Make a prediction
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)


prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
   print ('the person is not diabetic')
else:
   print('the person is diabetic')

def main():

  # Set the title and description of the app
    st.title('Diabetes prediction Web App')
    st.write('Enter the input features and get predictions for diabetes.')

    Pregnencies = st.text_input('Number of Pregnencies')
    Glucose = st.text_input('Glucose')
    BloodPressure = st.text_input('BloodPressure')
    SkinThickness = st.text_input('SkinThickness')
    Insulin = st.text_input('Insulin')
    BMI = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    Age = st.text_input('Age')

    diagnosis = ''

    if st.button('Diabetes Test Results'):
      diagnosis = diabetes_prediction([Pregnencies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)

if __name__ == '__main__':
    main()