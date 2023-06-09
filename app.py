import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.markdown("<h1 style='text-align: center; color:#3E3F3A; font-size:50px;'>HEART DISEASE PREDICTION</h1>", unsafe_allow_html=True)

heart_model = pickle.load(open('pipe.pkl', 'rb'))

def main():
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
    
    sex = 1 if sex == "Male" else 0
    cp_mapping = {"Typical angina": 0, "Atypical angina": 1, "Non-anginal pain": 2, "Asymptotic": 3}
    cp = cp_mapping[cp]
    restecg_mapping = {"Normal": 0, "ST-T wave abnormality": 1, "Left ventricular hypertrophy": 2}
    restecg = restecg_mapping[restecg]
    fbs = 1 if fbs == ">120 mg/dl" else 0
    exang = 1 if exang == "Yes" else 0
    slope_mapping = {"Upsloping": 0, "Flatsloping": 1, "Downsloping": 2}
    slope = slope_mapping[slope]
    thal_mapping = {"Normal": 0, "Fixed defect": 1, "Reversible defect": 2}
    thal = thal_mapping[thal]

    heart_pred = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if st.button("Predict"):
        if heart_pred[0] == 1:
            st.error('Warning! You have a high risk of getting a heart attack!')
        else:
            st.success('You have a lower risk of getting a heart disease!')
main()
st.text('Created by Mohamed Elgendy')
