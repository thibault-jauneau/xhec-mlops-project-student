import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression


def train_model(X_train, y_train):
    """Train a Linear Regression model and log the model with MLflow."""
    with mlflow.start_run():
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Logging the model to MLflow
        mlflow.sklearn.log_model(model, "linear_model")
        return model
