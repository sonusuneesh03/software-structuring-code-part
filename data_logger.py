#This module will handle saving the sensor data to a CSV file.

import pandas as pd

def save_to_csv(data_log, filename="copd_sensor_data.csv"):
    """
    Saves the sensor data log to a csv file.
    """
    df = pd.DataFrame(data_log)
    df.to_csv(filename, index=False)
    print(f"\nData saved to software structuring test1 \n")