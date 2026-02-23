import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("vehicle_price_model (1).pkl")

st.title("🚗 Vehicle Price Predictor")

# Input fields
make = st.selectbox("Select Make", ["Honda", "Hyundai", "Maruti"])
model_name = st.selectbox("Select Model", ["Civic", "i20", "Swift"])
year = st.slider("Year", 2000, 2025, 2020)
engine = st.number_input("Engine Size (in liters)", min_value=0.6, max_value=5.0, value=1.2)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
color = st.selectbox("Color", ["White", "Red", "Grey"])
drivetrain = st.selectbox("Drivetrain", ["FWD", "RWD"])

# Convert inputs to numeric (You should use same encoders used in training)
input_data = np.array([[1, 2, year, engine, 0, 1, 0, 1]])  # Dummy-encoded
# Replace above with your actual encodings

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Vehicle Price: ₹ {int(prediction[0])}")