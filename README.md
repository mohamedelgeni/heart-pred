# Heart-disease-prediction-webapp
This project aims to create a web app using streamlit library in python that helps you find out whether you are at a risk of developing a heart disease or not.

# About Problem
Heart disease is the leading cause of death worldwide, accounting for one third of deaths in 2019. Heart disease cases nearly doubled over the period, from 271 million in 1990 to 523 million in 2019, and the number of heart disease deaths rose from 12.1 million to 18.6 million. The efficient and accurate and early medical diagnosis of heart disease plays a crucial role in taking preventive measures to prevent death.

<img src="https://user-images.githubusercontent.com/73715927/180886155-645d8bc1-d396-4b7c-a7eb-b7507a9615f1.jpg" width="450" height="280">

# About Dataset
Heart Disease Cleveland UCI dataset has been used in this project which is available on Kaggle. 
The link of the dataset used is: https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci

There are 297 records of patients, with no null values. Also there are 13 attributes in the dataset as follows.

1.	age: age in years
2.	sex: sex (1 = male; 0 = female)
3.	cp: chest pain type -- Value 0: typical angina -- Value 1: atypical angina -- Value 2: non-anginal pain -- Value 3: asymptomatic
4.	trestbps: resting blood pressure (in mm Hg on admission to the hospital)
5.	chol: serum cholestoral in mg/dl
6.	fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
7.	restecg: resting electrocardiographic results -- Value 0: normal -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
8.	thalach: maximum heart rate achieved
9.	exang: exercise induced angina (1 = yes; 0 = no)
10.	oldpeak = ST depression induced by exercise relative to rest
11.	slope: the slope of the peak exercise ST segment -- Value 0: upsloping -- Value 1: flat -- Value 2: downsloping
12.	ca: number of major vessels (0-3) colored by flourosopy
13.	thal: 0 = normal; 1 = fixed defect; 2 = reversable defect and the label Target variable: condition: 0 = no disease, 1 = disease


I've deployed the machine learning model using streamlit library of python. The code for the web app can be found in the "app.py" file. The link of the web app is given below:

https://muskan123-b-heart-disease-prediction-webapp3-app-lb8dp5.streamlitapp.com/
