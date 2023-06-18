import requests
import json

input_data = {
    "Month": "Dec",
    "WeekOfMonth": 2,
    "DayOfWeek": "Monday",
    "Make": "Toyota",
    "AccidentArea": "Urban",
    "DayOfWeekClaimed": "Tuesday",
    "MonthClaimed": "Jan",
    "WeekOfMonthClaimed": 3,
    "Sex": "Female",
    "MaritalStatus": "Single",
    "Age": 25,
    "Fault": "Policy_Holder",
    "PolicyType": "Sedan___All_Perils",
    "VehicleCategory": "Sport",
    "VehiclePrice": "more_than_69000",
    "PolicyNumber": 12,
    "RepNumber": 7,
    "Deductible": 400,
    "DriverRating": 4,
    "Days_Policy_Accident": "more_than_30",
    "Days_Policy_Claim": "more_than_30",
    "PastNumberOfClaims": "1",
    "AgeOfVehicle": "5_years",
    "AgeOfPolicyHolder": "21_to_25",
    "PoliceReportFiled": "Yes",
    "WitnessPresent": "No",
    "AgentType": "External",
    "NumberOfSuppliments": "1_to_2",
    "AddressChange_Claim": "1_year",
    "NumberOfCars": "1_vehicle",
    "Year": 1994,
    "BasePolicy": "Collision"
}


# Convert the input data to JSON
payload = json.dumps(input_data)

# Set the headers for the request
headers = {'Content-Type': 'application/json'}

# Send a POST request to the API
response = requests.post('http://localhost:5000/predict', data=payload, headers=headers)

# Print the response
print(response.json())
