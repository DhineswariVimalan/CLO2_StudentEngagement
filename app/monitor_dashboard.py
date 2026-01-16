# monitor_dashboard.py
import streamlit as st
import pandas as pd

# --- Load logs CSV ---
try:
    logs = pd.read_csv("monitoring_logs.csv")
except FileNotFoundError:
    st.error("monitoring_logs.csv not found. Make sure your logs file exists.")
    st.stop()

st.title("Model Monitoring Dashboard")

# --- Show raw logs ---
st.subheader("Raw Monitoring Logs")
st.dataframe(logs.tail(10))  # Show last 10 rows

# --- Bar chart: Average latency per model ---
if "latency" in logs.columns and "model_version" in logs.columns:
    latency_data = logs.groupby("model_version")["latency"].mean().reset_index()
    st.subheader("Average Latency per Model")
    st.bar_chart(latency_data.set_index("model_version"))
else:
    st.warning("Latency data not available.")

# --- Bar chart: Average feedback score per model ---
if "feedback_score" in logs.columns and "model_version" in logs.columns:
    feedback_data = logs.groupby("model_version")["feedback_score"].mean().reset_index()
    st.subheader("Average Feedback Score per Model")
    st.bar_chart(feedback_data.set_index("model_version"))
else:
    st.warning("Feedback score data not available.")

# --- Recent comments ---
if "comments" in logs.columns:
    st.subheader("Recent Comments")
    recent_comments = logs["comments"].dropna().tail(5)
    if not recent_comments.empty:
        for idx, comment in enumerate(recent_comments, 1):
            st.write(f"{idx}. {comment}")
    else:
        st.info("No comments available.")
else:
    st.warning("Comments column not found.")