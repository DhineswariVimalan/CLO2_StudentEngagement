import streamlit as st
import pickle
import numpy as np

# Load model (use BEST model → v2)
with open('model_v2.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Student Engagement Prediction App")

st.write("Enter student activity details to predict engagement level")

# User inputs
total_clicks = st.number_input("Total Clicks", min_value=0)
active_days = st.number_input("Active Days", min_value=0)
interactive_clicks = st.number_input("Interactive Clicks", min_value=0)
content_clicks = st.number_input("Content Clicks", min_value=0)
inter_ratio = st.number_input("Interaction Ratio", min_value=0.0, step=0.01)

if st.button("Predict Engagement"):
    input_data = np.array([
        total_clicks,
        active_days,
        interactive_clicks,
        content_clicks,
        inter_ratio
    ]).reshape(1, -1)

    prediction = model.predict(input_data)

    st.success(f"Predicted Engagement Level: {prediction[0]}")