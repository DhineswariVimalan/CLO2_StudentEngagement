import csv
import os
from datetime import datetime

LOG_FILE = "data/monitoring_logs.csv"

def log_prediction(
    total_clicks,
    active_days,
    interactive_clicks,
    content_clicks,
    prediction_v1,
    prediction_v2,
    latency_ms,
    feedback
):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "total_clicks",
                "active_days",
                "interactive_clicks",
                "content_clicks",
                "prediction_v1",
                "prediction_v2",
                "latency_ms",
                "feedback"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            total_clicks,
            active_days,
            interactive_clicks,
            content_clicks,
            prediction_v1,
            prediction_v2,
            latency_ms,
            feedback
        ])