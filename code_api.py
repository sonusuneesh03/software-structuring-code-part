from flask import Flask, request, jsonify
import boto3
import time
from decimal import Decimal  # Import Decimal

# Initialize Flask app
app = Flask(__name__)

# Connect to AWS DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')  # Change to your AWS region
table = dynamodb.Table('COPDData')  # Use the table name you created

@app.route('/sensor_data', methods=['POST'])
def store_data():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Generate a timestamp
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

        # Convert float values to Decimal
        item = {
            'timestamp': timestamp,
            'sp02': Decimal(str(data['sp02'])),  # Convert to Decimal
            'heart_rate': Decimal(str(data['heart_rate'])),  # Convert to Decimal
            'breathing_rate': Decimal(str(data['breathing_rate'])),  # Convert to Decimal
            'temperature': Decimal(str(data['temperature'])),  # Convert to Decimal
            'hrv': Decimal(str(data['hrv'])),  # Convert to Decimal
            'resp_rate': Decimal(str(data['resp_rate'])),  # Convert to Decimal
            'cohb': Decimal(str(data['cohb'])),  # Convert to Decimal
            'paco2': Decimal(str(data['paco2']))  # Convert to Decimal
        }

        # Insert data into DynamoDB
        table.put_item(Item=item)

        # Return success response
        return jsonify({"message": "Data stored successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main block to run the Flask app and print the registered routes
if __name__ == '__main__':
    print("Registered Routes:")  # Print available routes
    print(app.url_map)  # Show all Flask routes
    app.run(debug=True, port=5000)

# Retrieve data from DynamoDB
response = table.scan()
print(response['Items'])


import logging

logging.basicConfig(level=logging.DEBUG)

@app.route('/sensor_data', methods=['POST'])
def store_data():
    logging.info('Received data: %s', request.json)
    # Your existing logic
