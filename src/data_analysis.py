import pandas as pd
import os

print("File running...")

# Get the project root directory
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))

# Create dataset path
dataset_path = os.path.join(project_root, "dataset", "creditcard.csv")

print("Dataset path:", dataset_path)

# Load dataset
df = pd.read_csv(dataset_path)

print("\nDataset Loaded Successfully")

print("\nFirst 5 Rows:")
print(df.head())

print("\nShape:", df.shape)