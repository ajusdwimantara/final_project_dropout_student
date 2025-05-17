import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('rf_model.pkl')

st.title("Student Dropout Prediction System")
st.write("""
This app predicts whether a student is at risk of **dropping out** or **graduating**, based on input features.
""")

# Input features
st.header("Student Information")

tuition_status = st.selectbox("Tuition Fees Up to Date?", ['Yes', 'No'])
grade_delta = st.slider("Grade Delta (Change in Grades)", -20.0, 20.0, 0.0, step=0.1)
age_at_enrollment = st.slider("Age at Enrollment", 17, 70, 20)
completion_delta = st.slider("Completion Ratio Delta", -1.0, 1.0, 0.0, step=0.01)
approval_delta = st.slider("Approval Rate Delta", -1.0, 1.0, 0.0, step=0.01)
has_scholarship = st.selectbox("Has Scholarship?", ['Yes', 'No'])

# Convert inputs to model-friendly format
input_df = pd.DataFrame({
    'Tuition_fees_up_to_date': [1 if tuition_status == 'Yes' else 0],
    'Grade_delta': [grade_delta],
    'Age_at_enrollment': [age_at_enrollment],
    'Completion_ratio_delta': [completion_delta],
    'Approval_rate_delta': [approval_delta],
    'Scholarship_holder': [1 if has_scholarship == 'Yes' else 0]
})

# Prediction
if st.button('Predict Dropout Risk'):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    if prediction == 'Dropout' or prediction == 1:
        st.error(f"⚠️ This student is at risk of dropping out. (Confidence: {proba[1]:.2f})")
    else:
        st.success(f"🎓 This student is likely to graduate. (Confidence: {proba[0]:.2f})")

