import streamlit as st
import pickle

# Rest of your code...

def main():
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        st.write("")
        age = st.sidebar.slider("AGE", 21, 81, 23)
        sex = st.sidebar.radio("GENDER (1=Male, 0=Female)", ["1", "0"])
        cp = st.sidebar.selectbox("CHEST PAIN (0=Typical angina, 1=Atypical angina, 2=Non—anginal pain, 3=Asymptotic)", ["0", "1", "2", "3"])
        trestbps = st.sidebar.slider("RESTING B.P.", 100, 400, 110)
        chol = st.sidebar.slider("CHOLESTEROL", 100, 400, 110)
        fbs = st.sidebar.radio("FASTING BLOOD SUGAR (1=fbs>120mg/dl, 0=fbs<120 mg/dl)", ["1", "0"])
    with col3:
        st.write("")
    with col1:
        st.write("")
        restecg = st.sidebar.selectbox("RESTING ECG (0=Normal ,1=Having ST-T wave abnormality, 2=Left ventricular hypertrophy)", ["0", "1", "2"])
        thalach = st.sidebar.slider("MAX. HEART BEAT ACHIEVED", 100, 200, 110)
        exang = st.sidebar.radio("EXERCISE INDUCED ANGINA(1=Yes, 0=No)", ["1", "0"])
    with col2:
        st.write("")
        oldpeak = st.sidebar.slider("ST DEPRESSION INDUCED", 0.0, 5.0, 0.5)
        slope = st.sidebar.radio("SLOPE OF THE PEAK EXERCISE ST SEGMENT (0=Upsloping, 1=Flatsloping, 2=Downsloping)", ["0", "1", "2"])
    with col3:
        st.write("")
        ca = st.sidebar.slider("NUMBER OF VESSELS (0-3) COLORED BY FLUOROSCOPY", 0, 3, 1)
        thal = st.sidebar.radio("THALASSEMIA (0 = normal; 1 = fixed defect; 2 = reversible defect)",["0", "1", "2"])

    # Rest of your code...

if __name__ == '__main__':
    main()
