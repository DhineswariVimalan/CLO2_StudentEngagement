import csv
import os
from datetime import datetime

LOG_FILE = "monitoring_logs.csv"

def log_prediction(
    total_clicks,
    active_days,
    interactive_clicks,
    content_clicks,
    v1_prediction,
    v2_prediction,
    latency,
    feedback
):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "total_clicks",
                "active_days",
                "interactive_clicks",
                "content_clicks",
                "v1_prediction",
                "v2_prediction",
                "latency",
                "feedback"
            ])

        writer.writerow([
            datetime.now(),
            total_clicks,
            active_days,
            interactive_clicks,
            content_clicks,
            v1_prediction,
            v2_prediction,
            latency,
            feedback
        ])