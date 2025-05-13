import streamlit as st
import pickle 
import numpy as np

crop_recommendation_model = pickle.load(open('RandomForest.pkl', 'rb'))


def recommend_crop(N, P, K, temp, humidity, pH, rainfall):
    pass

st.title("Crop Recommendation System")

N = st.number_input("Nitrogen (N)", min_value=1.0, max_value=100.0, value=1.0, step=0.1)
P = st.number_input("Phosphorous (P)", min_value=1.0, max_value=100.0, value=1.0, step=0.1)
K = st.number_input("Potassium (K)", min_value=1.0, max_value=100.0, value=1.0, step=0.1)
temp = st.number_input("Temperature (°C)", min_value=1.0, max_value=50.0, value=25.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=1.0, max_value=100.0, value=50.0, step=0.1)
pH = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=1.0, max_value=250.0, value=50.0, step=0.1)

if st.button("Predict"):
    data = np.array([[N, P, K, temp, humidity, pH, rainfall]])
    prediction = crop_recommendation_model.predict(data)
    st.write("You Should Grow"' ' +  prediction +' ' "in your farm.")












