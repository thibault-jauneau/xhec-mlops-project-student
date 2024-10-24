"""
This module contains the main Prefect flow for training a machine learning model to predict the age of abalone based on physical characteristics.

It also contains functionality to schedule regular retraining via Prefect Deployments.
"""

import argparse
import os
from pathlib import Path

import mlflow
import pandas as pd
from prefect import flow, task
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from preprocessing import preprocess_data
from training import train_model
from utils import pickle_object

# Set up MLflow tracking server URI
mlflow.set_tracking_uri("http://localhost:5000")
os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"


@task(name="read_data", retries=2)
def read_data(trainset_path: Path) -> pd.DataFrame:
    """Read the training data from a CSV file."""
    return pd.read_csv(trainset_path)


@task(name="save_model")
def save_model_task(
    model, path: str = "src/web_service/local_objects/model.pkl"
) -> None:
    """
    Save the trained model to disk as a pickle file.

    Args:
        model: The trained model to be saved.
        path (str): The file path where the model will be saved (default: 'src/web_service/local_objects/model.pkl').
    """
    pickle_object(model, path)


@flow(name="train_model_flow", log_prints=True)
def train_flow(trainset_path: str) -> None:
    """
    Execute the complete model training pipeline with data preprocessing and saving the model as a pickle.

    Args:
        trainset_path (str): Path to the CSV file containing the training dataset.
    """
    path = Path(trainset_path)

    df = read_data(path)
    X_train, X_test, y_train, y_test = preprocess_data(df)
    model = train_model(X_train, y_train)
    save_model_task(model)

    print("Model training and saving completed successfully.")


def create_deployment() -> None:
    """
    Create a Prefect deployment that schedules regular retraining of the model.

    The deployment is scheduled to run weekly at midnight on Sunday using a Cron expression.
    """
    deployment = Deployment.build_from_flow(
        flow=train_flow,
        name="weekly_model_training",
        schedule=CronSchedule(cron="0 0 * * 0"),  # Run weekly at midnight on Sunday
        tags=["training", "production"],
    )
    deployment.apply()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model using the data at the given path."
    )
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    parser.add_argument(
        "--create-deployment",
        action="store_true",
        help="Create a Prefect deployment for regular retraining",
    )
    args = parser.parse_args()

    if args.create_deployment:
        create_deployment()
    else:
        train_flow(args.trainset_path)
