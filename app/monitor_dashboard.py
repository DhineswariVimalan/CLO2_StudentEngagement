# monitor_dashboard.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Model Monitoring Dashboard", layout="wide")

st.title("📊 Model Monitoring Dashboard")

# --- Load logs CSV safely ---
try:
    logs_df = pd.read_csv("monitoring_logs.csv")
except FileNotFoundError:
    st.error("❌ monitoring_logs.csv not found. Run the prediction app first.")
    st.stop()

# --- Check if logs are empty ---
if logs_df.empty:
    st.warning("⚠️ Monitoring logs are empty.")
    st.stop()

# --- Show recent logs ---
st.subheader("📄 Recent Predictions (Last 10)")
st.dataframe(logs_df.tail(10), use_container_width=True)

# --- Average latency per model ---
if {"latency", "model_version"}.issubset(logs_df.columns):
    st.subheader("⏱️ Average Latency per Model")
    latency_data = (
        logs_df.groupby("model_version")["latency"]
        .mean()
        .reset_index()
        .set_index("model_version")
    )
    st.bar_chart(latency_data)
else:
    st.warning("Latency or model_version column missing.")

# --- Average feedback score per model ---
if {"feedback_score", "model_version"}.issubset(logs_df.columns):
    st.subheader("⭐ Average Feedback Score per Model")
    feedback_data = (
        logs_df.groupby("model_version")["feedback_score"]
        .mean()
        .reset_index()
        .set_index("model_version")
    )
    st.bar_chart(feedback_data)
else:
    st.warning("Feedback score or model_version column missing.")

# --- Recent comments ---
if "comments" in logs_df.columns:
    st.subheader("💬 Recent User Comments")
    recent_comments = logs_df["comments"].dropna().tail(5)

    if not recent_comments.empty:
        for i, comment in enumerate(recent_comments, 1):
            st.write(f"{i}. {comment}")
    else:
        st.info("No user comments available.")
else:
    st.warning("Comments column not found.")