import numpy as np
import pandas as pd
import time
import os

# Ensure the directory exists
folder_path = "/Users/sonusuneesh/Desktop/Thadickal/software structring test 1"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Created folder at: {folder_path}")

# Function to generate simulated COPD sensor data
def generate_copd_sensor_data():
    spo2 = np.random.normal(92, 3)  # Simulating SpO₂ (Normal range 95-100%, COPD < 90%)
    heart_rate = np.random.normal(70, 10)  # Simulating heart rate (Normal range 60-100 bpm, COPD < 60%)
    breathing_rate = np.random.normal(16, 2)  # Simulating breathing rate (Normal range 12-20 bpm, COPD < 12%)
    temperature = np.random.normal(37.3, 0.5)  # Simulating temperature (Normal range 36.5-37.8°C, COPD < 36.5°C)
    hrv = np.random.normal(40, 100)  # Simulating HRV (Normal 60-100ms)
    resp_rate = np.random.randint(12, 30)  # Simulating Respiratory Rate
    cohb = np.random.uniform(0.5, 5.0)  # Simulating Carboxyhemoglobin in %
    paco2 = np.random.uniform(35, 55)  # Simulating CO₂ levels in blood (PaCO₂)

    return {
        "sp02": round(spo2, 2),
        "heart rate": round(heart_rate, 2),
        "breathing rate": round(breathing_rate, 2),
        "temperature": round(temperature, 2),
        "hrv": round(hrv, 2),
        "resp rate": resp_rate,
        "cohb": round(cohb, 2),
        "paco2": round(paco2, 2),
        "timestamp": pd.Timestamp.now()
    }

# Run the simulation and store the data
data_logger = []  # Store data here
print("Generating COPD sensor sample data...\n")
while True:
    sensor_data = generate_copd_sensor_data()
    data_logger.append(sensor_data)
    print(sensor_data)
    time.sleep(2)  # Simulate data collection interval

    # Save data to CSV every 10 readings
    if len(data_logger) % 10 == 0:
        df = pd.DataFrame(data_logger)
        print(df.head())  # Print the first few rows of data for checking
        print("Generating COPD sensor data...")  # Ensure the loop is starting
        file_path = os.path.join(folder_path, "copd_sensor_data.csv")  # Join folder path and file name
        df.to_csv(file_path, index=False)
        print(f"\nData saved to {file_path}\n")
