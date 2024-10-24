# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.
import argparse
from pathlib import Path

import pandas as pd
from preprocessing import preprocess_data
from training import train_model
from utils import pickle_object


def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    # Read data
    df = pd.read_csv(trainset_path)

    # Preprocess data
    X_train, X_test, y_train, y_test = preprocess_data(df)

    # (Optional) Pickle encoder if need be

    # Train model
    model = train_model(X_train, y_train)

    # Pickle model --> The model should be saved in pkl format the `src/web_service/local_objects` folder
    pickle_object(model, "src/web_service/local_objects/model.pkl")
    print("Model training and saving completed successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model using the data at the given path."
    )
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
