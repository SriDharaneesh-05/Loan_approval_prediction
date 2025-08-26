import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -------------------- Load the trained model --------------------
# Replace 'your_model.pkl' with the filename of your saved model
model = joblib.load("model.pkl")

# -------------------- Streamlit UI --------------------
st.title("🏦 Loan Approval Prediction")

gender = st.radio("Gender", ["Male", "Female"])
married = st.radio("Married", ["Yes", "No"])
dependents = st.number_input("Dependents", min_value=0, value=0)
education = st.radio("Education", ["Graduate", "Not Graduate"])
self_employed = st.radio("Self Employed?", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0, value=5000)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0, value=0)
loan_amount = st.number_input("Loan Amount", min_value=0, value=100)
loan_term = st.number_input("Loan Term (months)", min_value=1, value=360)
credit_history = st.radio("Credit History", [1, 0])
property_area = st.radio("Property Area", ["Urban", "Semiurban", "Rural"])

# Convert categorical inputs to match training encoding
input_data = pd.DataFrame({
    "Gender": [1 if gender == "Male" else 0],
    "Married": [1 if married == "Yes" else 0],
    "Dependents": [dependents],
    "Education": [1 if education == "Graduate" else 0],
    "Self_Employed": [1 if self_employed == "Yes" else 0],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Loan_Amount_Term": [loan_term],
    "Credit_History": [credit_history],
    "Property_Area": [0 if property_area=="Rural" else (1 if property_area=="Semiurban" else 2)]
})

# Prediction
if st.button("Predict Loan Approval"):
    prediction = model.predict(input_data)
    result = "✅ Approved" if prediction[0] == 1 else "❌ Not Approved"
    st.subheader(f"Loan Status: {result}")