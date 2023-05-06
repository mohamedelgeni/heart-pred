import streamlit as st
import pickle

# Setting the page title and layout
st.set_page_config(page_title='Heart Disease Prediction', layout='wide')

# Loading the trained model
heart_model = pickle.load(open('pipe.pkl', 'rb'))

# Page title and description
st.markdown("<h1 style='text-align: center; color:#42D1C6; font-size:50px;'>HEART DISEASE PREDICTION WEBAPP</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:#d5e1df; font-size:25px;'>This web app aims to help you find out whether you are at risk of developing a heart disease or not</p>", unsafe_allow_html=True)

def main():
    # Getting the input data from the user
    st.write('### Input Parameters')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider("AGE", 11, 81, 23)
        trestbps = st.slider("RESTING B.P.", 100, 400, 110)
        restecg = st.selectbox("RESTING ECG", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
        oldpeak = st.slider("ST DEPRESSION INDUCED", 0.0, 5.0, 0.5)
    with col2:
        sex = st.radio("GENDER", ["Male", "Female"])
        chol = st.slider("CHOLESTEROL", 100, 400, 110)
        thalach = st.slider("MAX. HEART BEAT ACHIEVED", 100, 200, 110)
        slope = st.selectbox("SLOPE OF THE PEAK EXERCISE ST SEGMENT", ["Upsloping", "Flatsloping", "Downsloping"])
    with col3:
        cp = st.selectbox("CHEST PAIN", ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptotic"])
        fbs = st.radio("FASTING BLOOD SUGAR", ["<120 mg/dl", ">120 mg/dl"])
        exang = st.radio("EXERCISE INDUCED ANGINA", ["No", "Yes"])
        ca = st.slider("NUMBER OF VESSELS COLORED BY FLUOROSCOPY", 0, 3, 1)
    
    thal = st.selectbox("THALASSEMIA", ["Normal", "Fixed defect", "Reversible defect"])
    
    # Code for prediction
    heart_pred = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    if st.button("Predict"):
        if heart_pred[0] == 1:
            st.error('Warning! You have a high risk of getting a heart attack!')
            st.write(f"Model Prediction: {heart_pred[0]} (1 = Heart disease present, 0 = No heart disease)")
        else:
            st.success('You have a lower risk of getting a heart disease!')
            st.write(f"Model Prediction: {heart_pred[0]} (1 = Heart disease present, 0 = No heart disease)")

if __name__ == '__main__':
    main()
