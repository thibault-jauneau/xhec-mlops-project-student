"""Preprocessing utilities for the abalone dataset."""
import pandas as pd
from prefect import task
from sklearn.model_selection import train_test_split


@task
def preprocess_data(df: pd.DataFrame):
    """Preprocess the abalone dataset.

    This function:
    1. Creates a target variable 'Age' by adding a constant to the 'Rings' column
    2. Drops unnecessary columns from the feature set
    3. Splits the dataset into training and testing sets

    Args:
        df: The input DataFrame containing the abalone dataset

    Returns:
        tuple: (X_train, X_test, y_train, y_test) containing the split datasets
    """
    # Create the target variable 'Age' by adding a constant to 'Rings'
    df["Age"] = df["Rings"] + 1.5

    # Drop unnecessary columns from the dataset
    X = df.drop(columns=["Rings", "Age", "Sex"])
    y = df["Age"]

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test
