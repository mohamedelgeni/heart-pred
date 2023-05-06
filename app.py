import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image
import base64

st.markdown("<h1 style='text-align: center; color:#42D1C6; font-size:50px;'>HEART DISEASE PREDICTION WEBAPP💗🩹</h1>",unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:#HEX: #d5e1df; font-size:25px;'>This web app aims to help you find out whether you are at a risk of developing a heart disease or not.</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:20px;'>Please select the required fields below!</p>",unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image("http://media.giphy.com/media/zXV7D35X56RQk/giphy.gif", width=270)
with col3:
    st.write(' ')

heart_model = pickle.load(open('pipe.pkl','rb'))

def main():
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
         age = st.sidebar.slider("AGE", 21, 81, 23)
    with col2:
         sex = st.sidebar.radio("GENDER (1=Male, 0=Female)", ["1", "0"])
    with col3:   
        cp = st.sidebar.selectbox(
        "CHEST PAIN (0=Typical angina, 1=Atypical angina, 2=Non—anginal pain, 3=Asymptotic)", ["0", "1", "2", "3"])
    with col1:
        trestbps = st.sidebar.slider("RESTING B.P.", 100, 400, 110)
    with col2:
        chol = st.sidebar.slider("CHOLESTEROL", 100, 400, 110)
    with col3:
        fbs = st.sidebar.radio(
        "FASTING BLOOD SUGAR (1=fbs>120mg/dl, 0=fbs<120 mg/dl)", ["1", "0"])
    with col1:
        restecg = st.sidebar.selectbox(
        "RESTING ECG (0=Normal ,1=Having ST-T wave abnormality, 2=Left ventricular hyperthrophy)", ["0", "1", "2"])
    with col2:
        thalach = st.sidebar.slider("MAX. HEART BEAT ACHIEVED", 100, 200, 110)
    with col3:
        exang = st.sidebar.radio(
        "EXERCISE INDUCED ANGINA(1=Yes, 0=No)", ["1", "0"])
    with col1:
        oldpeak = st.sidebar.slider(
        "ST DEPRESSION INDUCED", 0.0, 5.0, 0.5)
    with col2:
        slope = st.sidebar.radio(
        "SLOPE OF THE PEAK EXERCISE ST SEGMENT (0=Upsloping, 1=Flatsloping, 2=Downsloping)", ["0", "1", "2"])
    with col3:
        ca = st.sidebar.slider(
        "NUMBER OF VESSELS (0-3) COLORED BY FLUOROSCOPY", 0, 3, 1)
    with col2:
        thal = st.sidebar.radio(
        "THALASSEMIA (0 = normal; 1 = fixed defect; 2 = reversable defect)",["0", "1", "2"])
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    heart_pred = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

    if st.button("Predict"):    
        if heart_pred[0] == 1:
            st.error('Warning! You have high risk of getting a heart attack!')
            st.write(f"Model Prediction: {heart_pred[0]} (1 = Heart disease present, 0 = No heart disease)")
        else:
            st.success('You have lower risk of getting a heart disease!')
            st.write(f"Model Prediction: {heart_pred[0]} (1 = Heart disease present, 0 = No heart disease)")
          
if __name__ == '__main__':
    main()
    
