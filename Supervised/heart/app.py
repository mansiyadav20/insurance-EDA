import streamlit as st
import pandas as pd
import joblib

model=joblib.load("knn_heart_model.pkl")
scaler=joblib.load("scaler.pkl")
columns=joblib.load("columns.pkl")

st.title("Heart Disease Prediction")
st.markdown("Provide the following details:")

age=st.slider("Age",min_value=18,max_value=100,value=30)
sex=st.selectbox("Sex",options=["Male","Female"])
chestpain=st.selectbox("Chest Pain Type",options=["ATA","NAP","TA","ASY"])
resting_bp=st.number_input("Resting Blood Pressure",min_value=80,max_value=200,value=120)
chlestrol=st.number_input("Cholesterol",min_value=100,max_value=600,value=200)
fasting_bs=st.selectbox("Fasting Blood Sugar>120",options=["True","False"])
resting_ecg=st.selectbox("Resting ECG",options=["Normal","ST","LVH"])
max_heart_rate=st.slider("Max Heart Rate",min_value=60,max_value=220,value=150)
exercise_angina=st.selectbox("Exercise Induced Angina",options=["Yes","No"])
oldpeak=st.slider("Old Peak",min_value=0.0,max_value=6.0,value=1.0)
st_slope=st.selectbox("ST Slope",options=["Up","Flat","Down"])

if st.button("Predict"):
    raw_data={
        "Age":age,
        "Sex":1 if sex=="female" else 0,
        "ChestPainType":chestpain,  
        "RestingBP":resting_bp,
        "Cholesterol":chlestrol,    
        "FastingBS":1 if fasting_bs=="True" else 0,
        "RestingECG":resting_ecg,
        "MaxHR":max_heart_rate,
        "ExerciseAngina":1 if exercise_angina=="Yes" else 0,
        "Oldpeak":oldpeak,
        "ST_Slope":st_slope
        
    }

    input_data=pd.DataFrame([raw_data])

    for cols in columns:
        if cols not in input_data.columns:
            input_data[cols]=0

    input_data=input_data[columns]
    scaled_data=scaler.transform(input_data)
    prediction=model.predict(scaled_data)

    if prediction[0]==1:
        st.error("The person is likely to have heart disease.")
    else:
        st.success("The person is unlikely to have heart disease.")

    