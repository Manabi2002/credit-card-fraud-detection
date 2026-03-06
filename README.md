# Credit Card Fraud Detection

This project uses Machine Learning to detect fraudulent credit card transactions.

## Project Overview
The system analyzes transaction data and predicts whether a transaction is fraudulent or normal using a Logistic Regression model.

## Features
- Data preprocessing
- Model training using Logistic Regression
- Fraud prediction system
- Example transaction testing

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn

## Dataset
Due to GitHub file size limits, the dataset is not included in this repository.

Download it from:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Place the dataset inside the `dataset` folder before running the project.

## Run the Project

Train the model:
## Project Structure

credit-card-fraud-detection/
│
├── src/
│   ├── data_preprocessing.py
│   ├── data_analysis.py
│   ├── train_model.py
│   └── predict.py
│
├── models/
│   └── fraud_model.pkl
│
├── dataset/
│   └── creditcard.csv (download from Kaggle)
│
├── templates/
│   └── index.html
│
├── README.md
└── requirements.txt