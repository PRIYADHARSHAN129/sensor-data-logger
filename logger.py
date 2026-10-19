import csv
from datetime import datetime


def save_readings(readings, filename="readings.csv"):
    """Save a list of readings to a CSV file with timestamps."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "distance_cm"])
        for value in readings:
            timestamp = datetime.now().isoformat(timespec="seconds")
            writer.writerow([timestamp, value])