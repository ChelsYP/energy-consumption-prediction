import streamlit as st
import pandas as pd
import joblib

# Load model & feature columns
model = joblib.load("models/energy_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

st.title("🔋 Energy Consumption Prediction")

st.write("Masukkan parameter bangunan untuk memprediksi konsumsi energi")

inputs = {}

inputs["Temperature"] = st.number_input("Temperature", value=20.0)
inputs["Humidity"] = st.number_input("Humidity", value=50.0)
inputs["SquareFootage"] = st.number_input("Square Footage", value=100.0)
inputs["Occupancy"] = st.number_input("Occupancy", value=1)

inputs["HVACUsage"] = st.selectbox("HVAC Usage", ["Off", "On"])
inputs["LightingUsage"] = st.selectbox("Lighting Usage", ["Off", "On"])

inputs["RenewableEnergy"] = st.number_input("Renewable Energy", value=0.0)
inputs["DayOfWeek"] = st.slider("Day of Week (0=Mon)", 0, 6, 0)
inputs["Holiday"] = st.selectbox("Holiday", ["No", "Yes"])

# Convert categorical
inputs["HVACUsage"] = 1 if inputs["HVACUsage"] == "On" else 0
inputs["LightingUsage"] = 1 if inputs["LightingUsage"] == "On" else 0
inputs["Holiday"] = 1 if inputs["Holiday"] == "Yes" else 0

df = pd.DataFrame([inputs])

# Ensure column order
df = df[feature_columns]

if st.button("Predict Energy Consumption"):
    prediction = model.predict(df)[0]
    st.success(f"🔮 Predicted Energy Consumption: {prediction:.2f}")
