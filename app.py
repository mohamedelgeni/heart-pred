import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image
import base64

st.markdown("<h1 style='text-align: center; color:#42D1C6; font-size:50px;'>HEART DISEASE PREDICTION WEBAPP</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:#HEX: #d5e1df; font-size:25px;'>This web app aims to help you find out whether you are at risk of developing a heart disease or not.</p>", unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def load_model():
    return pickle.load(open('pipe.pkl', 'rb'))

heart_model = load_model()

def main():
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("AGE", min_value=1, max_value=120, step=1, value=23)
        trestbps = st.number_input("RESTING B.P.", min_value=50, max_value=250, step=1, value=110)
        restecg = st.selectbox("RESTING ECG", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
        oldpeak = st.number_input("ST DEPRESSION INDUCED", min_value=0.0, max_value=10.0, step=0.1, value=0.5)
    with col2:
        sex = st.radio("GENDER", ["Male", "Female"])
        chol = st.number_input("CHOLESTEROL", min_value=50, max_value=600, step=1, value=200)
        thalach = st.number_input("MAX. HEART BEAT ACHIEVED", min_value=50, max_value=250, step=1, value=150)
        slope = st.selectbox("SLOPE OF THE PEAK EXERCISE ST SEGMENT", ["Upsloping", "Flatsloping", "Downsloping"])
    with col3:
        cp = st.selectbox("CHEST PAIN", ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptotic"])
        fbs = st.selectbox("FASTING BLOOD SUGAR", ["<120 mg/dl", ">120 mg/dl"])
        exang = st.selectbox("EXERCISE INDUCED ANGINA", ["No", "Yes"])
        ca = st.number_input("NUMBER OF VESSELS COLORED BY FLUOROSCOPY", min_value=0, max_value=3, step=1, value=1)
        thal = st.selectbox("THALASSEMIA", ["Normal", "Fixed defect", "Reversible defect"])
    
    # Code for prediction
    diagnosis = ''
    
    input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    heart_pred = heart_model.predict(input_data)
    
    if st.button("Predict"):    
        if heart_pred[0] == 1:
            st.error('Warning! You have high risk of getting a heart attack!')
            st.write(f"Model Prediction: {heart_pred[0]} (1 = Heart disease present, 0 = No heart disease)")
        else:
            st.success('You have lower risk of getting a heart disease!')
            st.write(f"Model Prediction: {heart_pred[0]} (1 = Heart disease present, 0 = No heart disease)")
          
if __name__ == '__main__':
    main()
