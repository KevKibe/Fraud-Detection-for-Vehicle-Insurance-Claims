# Problem Statement
Fitting a model that will be able to classify a vehicle insurance claim as either fraud or legitimate.

# Dataset
The data used are samples of vehicle claim data with a target variable as fraud represented as 1 and legitimate represented as 0.

  
## Installation
1. Clone the repository: `git clone https://github.com/KevKibe/Fraud-Detection-for-Vehicle-Insurance-Claims`
2. Navigate to the project directory: `cd Fraud-Detection-for-Vehicle-Insurance-Claims`
3. Install the dependencies: `pip install -r requirements.txt`
## Usage
1. Start the Flask API: `python main.py`
2. Access the web interface at: `https://claim-fraud-detection-f5m2fxxbbq-uc.a.run.app` or your local server `http://localhost:5000`
3. 3. Run the model on test data: `python test.py`


## Deploying and Containerizing Your Application with Docker

Before you start, make sure you have [Docker](https://www.docker.com/get-started) installed on your system. 


1. **Clone the Repository:** First, clone the repository for your application to your local machine or cloud instance using the following commands:
   ```sh
   git clone https://github.com/KevKibe/Fraud-Detection-for-Vehicle-Insurance-Claims.git
   cd Fraud-Detection-for-Vehicle-Insurance-Claims
2.**Build the Docker Image:** Replace your-app-name with a suitable name for your application.
   ```
   docker build -t your-app-name .

 ```



## To deploy on an AWS EC2 instance
- Setup an EC2 instance and SSH to the instance.Use this as a [guide](https://www.machinelearningplus.com/deployment/deploy-ml-model-aws-ec2-instance/).
- Run
   ```
  git clone https://github.com/KevKibe/Fraud-Detection-for-Vehicle-Insurance-Claims.git
  ```
- Start up [Docker](https://docs.docker.com) and run
  ```
  docker build -t dockerfile .
  ```
- run
  ```
  docker run -e PORT=8080 dockerfile
  ```
- You can now get predictions from
  ```
  http://<ec2-public-IP>:8080/predict
  ```
