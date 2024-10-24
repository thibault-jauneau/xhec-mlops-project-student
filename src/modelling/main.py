"""Train a model using Prefect flows and tasks."""
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
    """Read training data from CSV file."""
    return pd.read_csv(trainset_path)


@task(name="save_model")
def save_model_task(
    model, path: str = "src/web_service/local_objects/model.pkl"
) -> None:
    """Save the trained model to disk."""
    pickle_object(model, path)


@flow(name="train_model_flow", log_prints=True)
def train_flow(trainset_path: str) -> None:
    """Execute the complete model training pipeline.

    Args:
        trainset_path: Path to the training dataset
    """
    path = Path(trainset_path)

    df = read_data(path)
    X_train, X_test, y_train, y_test = preprocess_data(df)
    model = train_model(X_train, y_train)
    save_model_task(model)

    print("Model training and saving completed successfully.")


def create_deployment() -> None:
    """Create a weekly deployment for the training flow."""
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
