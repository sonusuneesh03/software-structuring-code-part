import joblib 
import pandas as pd

#load the trained model 
model = joblib.load('copd_model_ai.pkl')

#new data 
new_data ={
    "sp02": 92,
    "heart rate": 80,
    "breathing rate": 26,
    "temperature": 37.5,
    "hrv": 30,
    "resp rate": 32,
    "cohb": 0.9,
    "paco2": 42
}

#convert the new data into a dataframe with pandas

new_data_df = pd.DataFrame(new_data, index=[0])

#make predictions
prediction = model.predict(new_data_df)

#print the prediction (1 for worsening, 0 for normal )

if prediction == 1:
    print("prediction: worsening condition")
else:
    print("prediction: normal condition"  )

prediction_df = new_data_df.copy()
prediction_df['prediction'] = prediction

#appened the result to an existing csv 
prediction_df.to_csv('prediction.csv', mode='a', header=False, index=False)
print(f"predition saved to 'predictions.csv'.")