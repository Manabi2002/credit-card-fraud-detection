import pickle
import os
import numpy as np

# Get project root
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))

# Load trained model
model_path = os.path.join(project_root, "models", "fraud_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)


def predict_transaction(features):

    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)

    if prediction[0] == 1:
        return "Fraud Transaction"
    else:
        return "Normal Transaction"


# Example test
if __name__ == "__main__":

    sample_transaction = [
        0.0, -1.359807, -0.072781, 2.536346, 1.378155,
        -0.338321, 0.462388, 0.239599, 0.098698, 0.363787,
        0.090794, -0.551600, -0.617801, -0.991390, 1.468177,
        -0.311169, 1.234567, -0.456789, 0.123456, 0.098765,
        -0.123456, 0.345678, -0.234567, 0.456789, 0.567890,
        -0.678901, 0.789012, -0.890123, 0.901234, 149.62
    ]

    result = predict_transaction(sample_transaction)

    print("\nPrediction Result:", result)