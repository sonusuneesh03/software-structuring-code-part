import requests
import json

# Load the JSON data from the file
with open('sensor_data.json', 'r') as file:
    sensor_data = json.load(file)

# Send a POST request to the Flask API
response = requests.post("http://127.0.0.1:5000/sensor_data", json=sensor_data)

# Print the raw response for debugging
print("Raw Response:", response.text)

# Check if the response contains valid JSON
if response.headers.get("Content-Type") == "application/json":
    print(response.json())
else:
    print("Error: Server returned non-JSON response")

