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
st.dataframe(logs_df.tail(100), use_container_width=True)[web:5]

## Model Behavior Insights
st.subheader("Model Behavior Interpretation")
latency_trend = px.line(logs_df.sort_values('timestamp'), x='timestamp', y='latency', title="Latency Trend Over Time")
st.plotly_chart(latency_trend, use_container_width=True)
if avg_latency > 1.0:
    st.error("⚠️ High average latency detected - investigate model inference.")
if avg_feedback < 4.0:
    st.warning("📉 Low feedback scores - check for data drift or model degradation.")
if error_rate > 5:
    st.error("🚨 High error rate - review recent logs for patterns.")[web:8][web:5]