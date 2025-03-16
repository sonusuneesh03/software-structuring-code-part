# This script will use the sensor_simulator and data_logger modules to simulate data and save it periodically.

import time
from sensorsimulaton import generate_copd_sensor_data
from data_logger import save_to_csv

#run the simulation and store the data 
data_logger = []
print("Generating copd sensor data..\n")

try:
    while True:
        #genrste sensor data 
        sensor_data = generate_copd_sensor_data()
        data_logger.append(sensor_data)
        print(sensor_data)
       
        
        #save data to csv every 10 readings
        if len(data_logger) % 10 == 0:
            save_to_csv(data_logger)
        
        #simulate real time updates 
        time.sleep(2)  # 2 seconds
except KeyboardInterrupt:
    print("\nSimulation stopped by user.")

