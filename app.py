import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("rain_model.pkl")

st.title(" Rainfall Prediction App")
st.write("Stacked Ensemble Model (RF + GB + XGBoost)")

# Inputs
avg_temp = st.slider("Avg Temperature", -10, 45, 25)
max_temp = st.slider("Max Temperature", -10, 50, 30)
min_temp = st.slider("Min Temperature", -20, 40, 20)
wind_speed = st.slider("Wind Speed", 0, 30, 5)
wind_dir = st.slider("Wind Direction", 0, 360, 180)

if st.button("Predict"):

    input_data = np.array([[avg_temp, max_temp, min_temp, wind_speed, wind_dir]])

    prob = model.predict_proba(input_data)[0][1]
    prob_percent = prob * 100
    prediction = 1 if prob > 0.45 else 0
    
    if prediction == 1:
        st.success(f" Rain Expected (Probability: {prob_percent:.2f}%)")
    else:
        st.info(f"☀️ No Rain (Probability: {prob_percent:.2f}%)")
