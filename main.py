from flask import Flask, request, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model= pickle.load(open('model1.pickle','rb'))
encoder = pickle.load(open('encoder1.pkl','rb'))
column_names= pickle.load(open('features1.pkl','rb'))
 

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()

    # Prepare the input dataframe
    df = pd.DataFrame(input_data, index=[0])

    # Ensure that the feature names in the input data match those that were used to train the model and fit the encoder
    columns_to_encode = ['Month', 'DayOfWeek', 'Make', 'AccidentArea', 'DayOfWeekClaimed', 'MonthClaimed', 'Sex', 'MaritalStatus', 'Fault', 'PolicyType', 'VehicleCategory', 'VehiclePrice', 'Days_Policy_Accident', 'Days_Policy_Claim', 'PastNumberOfClaims', 'AgeOfVehicle', 'AgeOfPolicyHolder', 'PoliceReportFiled', 'WitnessPresent', 'AgentType',
                         'NumberOfSuppliments', 'AddressChange_Claim', 'NumberOfCars', 'BasePolicy']
    df = df.loc[:, columns_to_encode]

    to_encode = [input_data[col] for col in columns_to_encode]
    encoded_features = list(encoder.transform(np.array(to_encode).reshape(1,-1))[0])

    # Input array
    to_predict = [input_data[feature] for feature in column_names if feature not in columns_to_encode]
    input_data = to_predict + encoded_features
    input_columns = [feature for feature in column_names if feature not in columns_to_encode] + list(encoder.get_feature_names_out(columns_to_encode))
    df_encoded = pd.DataFrame([input_data], columns=input_columns)

    # Perform prediction using the loaded model
    prediction = model.predict(df_encoded)
    prediction_text = ["Fraud" if pred == 1 else "Legitimate" for pred in prediction]
    return jsonify({'prediction': prediction_text})



if __name__ == '__main__':
    app.run()
