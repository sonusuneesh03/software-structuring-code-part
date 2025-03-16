# Ai modeling and structring generation

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#import the existing data 

df = pd.read_csv("copd_sensor_data.csv")

df['label'] = ((df['sp02'] < 90) | 
               (df['heart rate'] > 100) | 
               (df['breathing rate'] < 10) | 
               (df['temperature'] > 38) |  #  fever could indicate worsening
               (df['resp rate'] < 12) |
               (df['paco2'] > 50) |
               (df['cohb'] > 3)).astype(int)  



# x = sensor data , y = labels for it 
x = df[['sp02','heart rate','breathing rate','temperature','hrv','resp rate','cohb','paco2']] #features input data
y = df['label'] #labels , output data

""" #check
print("Features shape:",x.shape)
print("Labels shape:",y.shape) """

#split the data into training and testing sets (80% training and 20% test sets)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print("Training data shape: ",x_train.shape)
print("Testing data shape: ",x_test.shape)

#training a machine learning model - Logistic Regression

model = LogisticRegression()
model.fit(x_train, y_train)

#make predictions on the test
y_pred = model.predict(x_test)

#evaluate the model performance

accuracy = accuracy_score(y_test,y_pred)
conf_matrix = confusion_matrix(y_test,y_pred)
class_report = classification_report(y_test,y_pred)

print("model accuracy:", accuracy)
print("confusion matrix:\n", confusion_matrix)
print("classification report:\n", class_report)




# save the model to a file using joblib (for large datasets)
import joblib


joblib.dump(model,'copd_model_ai.pkl')
print("model saved to 'copd_model_ai.pkl'")