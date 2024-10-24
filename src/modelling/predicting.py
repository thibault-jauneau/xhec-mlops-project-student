import pickle
import pandas as pd

def load_model(model_path):
    """Load the pickled model from the specified path."""
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model

def predict(input_data, model_path="src/web_service/local_objects/model.pkl"):
    """Make predictions using the loaded model."""
    model = load_model(model_path)
    predictions = model.predict(input_data)
    return predictions
