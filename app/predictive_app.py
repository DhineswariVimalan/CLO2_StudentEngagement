import streamlit as st
import pandas as pd
import time
from utils.log_utils import log_prediction  # make sure log_utils.py is in utils/

# --- Page Config ---
st.set_page_config(page_title="Student Engagement Predictor", layout="centered")
st.title("Student Engagement Prediction App")

# --- Input Fields ---
st.header("Enter Student Activity Data")
total_clicks = st.number_input("Total Clicks", min_value=0, step=1, value=10)
active_days = st.number_input("Active Days", min_value=1, step=1, value=5)
interactive_clicks = st.number_input("Interactive Clicks", min_value=0, step=1, value=3)
content_clicks = st.number_input("Content Clicks", min_value=0, step=1, value=2)

# --- Predict Button ---
if st.button("Predict Engagement"):

    # Record start time
    start_time = time.time()

    # --- Prediction Logic ---
    # v1: simple weighted sum
    v1_prediction = (0.4 * total_clicks) + (0.3 * active_days) + (0.2 * interactive_clicks) + (0.1 * content_clicks)
    
    # v2: adjusted formula with squared interactive clicks (example improvement)
    v2_prediction = (0.3 * total_clicks) + (0.25 * active_days) + (0.3 * (interactive_clicks ** 1.5)) + (0.15 * content_clicks)

    # Record end time
    end_time = time.time()
    latency = round(end_time - start_time, 4)  # in seconds

    # --- Display Predictions ---
    st.subheader("Predictions")
    st.write(f"**v1 Prediction:** {round(v1_prediction, 2)}")
    st.write(f"**v2 Prediction:** {round(v2_prediction, 2)}")
    st.write(f"**Latency:** {latency} seconds")

    # --- Feedback Section ---
    st.subheader("Submit Feedback")
    feedback_type = st.selectbox("Select Feedback Type", ["Rating", "Comment"])
    feedback_value = None

    if feedback_type == "Rating":
        feedback_value = st.slider("Rate Prediction Accuracy (1=Poor, 5=Excellent)", 1, 5, 3)
    else:
        feedback_value = st.text_area("Your Comments", "")

    if st.button("Submit Feedback"):
        # Log feedback to CSV using log_utils
        log_prediction(
            total_clicks=total_clicks,
            active_days=active_days,
            interactive_clicks=interactive_clicks,
            content_clicks=content_clicks,
            v1_prediction=v1_prediction,
            v2_prediction=v2_prediction,
            latency=latency,
            feedback=feedback_value
        )
        st.success("Feedback submitted successfully!")