import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Get project root
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))

# Dataset path
dataset_path = os.path.join(project_root, "dataset", "creditcard.csv")

# Load dataset
df = pd.read_csv(dataset_path)

print("Dataset Loaded")

# Split features and target
X = df.drop("Class", axis=1)
y = df["Class"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Data Split Completed")

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model Training Completed")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save model
model_path = os.path.join(project_root, "models", "fraud_model.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("Model Saved Successfully")