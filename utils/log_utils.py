import csv
import os
from datetime import datetime

LOG_FILE = "monitoring_logs.csv"

def log_prediction(model_version, prediction, latency):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "model_version", "prediction", "latency"])
        writer.writerow([
            datetime.now(),
            model_version,
            prediction,
            latency
        ])