# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:16:36 2023

@author: abah2
"""

#!pip install streamlit
import numpy as np
import pickle
import streamlit as st

#loaded_model= pickle.load(open('C:\Users\abah2\Documents\Python Scripts\Test Streamlit new\trained_model.sav', 'rb'))

#import pickle

import os
#import pickle

# Define the file path
file_path = 'C:/Users/abah2/Documents/Python Scripts/Test Streamlit new/trained_model.sav'

# Check if the file exists
if os.path.exists(file_path):
    print('The file exists.')
else:
    print('The file does not exist or the path is incorrect.')
    
    # Load the trained model
with open(file_path, 'rb') as file:
    loaded_model = pickle.load(file)

# Use the loaded model to make predictions
...

# Load the trained model
#with open('content/trained_model.sav', 'rb') as file:
    #loaded_model = pickle.load(file)

# Use the loaded model to make predictions
...

def diabetes_prediction(input_data):

  input_data_as_numpy_array = np.asarray(input_data)

# Define the input data
input_data = [6, 148, 72, 35, 0, 33.6, 0.627, 50]

# Reshape the input data
input_data_reshaped = np.array(input_data).reshape(1, -1)

# Make a prediction
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