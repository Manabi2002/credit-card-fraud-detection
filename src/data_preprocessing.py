import pandas as pd

def load_data():

    # Load dataset
    data = pd.read_csv("dataset/creditcard.csv")

    print("Dataset Loaded Successfully\n")

    print("First 5 Rows:")
    print(data.head())

    print("\nDataset Shape:")
    print(data.shape)

    return data


if __name__ == "__main__":
    load_data()