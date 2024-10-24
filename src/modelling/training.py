import mlflow
import mlflow.sklearn
from prefect import task
from sklearn.linear_model import LinearRegression


@task
def train_model(X_train, y_train):
    """
    Prefect task to train a Linear Regression model and log it using MLflow.

    This function:
    1. Initializes a Linear Regression model.
    2. Trains the model on the provided training data.
    3. Logs the trained model to MLflow for future reference and deployment.

    Args:
        X_train (pd.DataFrame): The feature set used for training.
        y_train (pd.Series): The target variable for training.

    Returns:
        model (LinearRegression): The trained Linear Regression model.
    """
    # Start an MLflow run for logging model training details
    with mlflow.start_run():
        # Initialize the Linear Regression model
        model = LinearRegression()

        # Train the model on the training data
        model.fit(X_train, y_train)

        # Log the trained model to MLflow for reproducibility and future use
        mlflow.sklearn.log_model(model, "linear_model")

    # Return the trained model
    return model
