# predictive_app.py

import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ✅ Add project root to Python path so 'utils' can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now the import will work
from utils.log_utils import log_prediction

# Other imports
import streamlit as st
import pickle
import pandas as pd
import time

# -------------------------------
# Load your models
# -------------------------------
model_v1_path = os.path.join(BASE_DIR, "models", "model_v1.pkl")
model_v2_path = os.path.join(BASE_DIR, "models", "model_v2.pkl")

with open(model_v1_path, "rb") as f:
    model_v1 = pickle.load(f)

with open(model_v2_path, "rb") as f:
    model_v2 = pickle.load(f)

# -------------------------------
# Streamlit App
# -------------------------------
st.title("Student Engagement Prediction App")

# Input fields
total_clicks = st.number_input("Total Clicks", min_value=0, step=1)
active_days = st.number_input("Active Days", min_value=0, step=1)
interactive_clicks = st.number_input("Interactive Clicks", min_value=0, step=1)
content_clicks = st.number_input("Content Clicks", min_value=0, step=1)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'total_clicks': [total_clicks],
        'active_days': [active_days],
        'interactive_clicks': [interactive_clicks],
        'content_clicks': [content_clicks]
    })

    start_time = time.time()
    
    pred_v1 = model_v1.predict(input_data)[0]
    pred_v2 = model_v2.predict(input_data)[0]
    
    latency = round(time.time() - start_time, 4)
    
    st.write(f"Model V1 Prediction: {pred_v1}")
    st.write(f"Model V2 Prediction: {pred_v2}")
    st.write(f"Prediction latency: {latency} seconds")
    
    # Log the prediction
    log_prediction(input_data, pred_v1, pred_v2, latency)