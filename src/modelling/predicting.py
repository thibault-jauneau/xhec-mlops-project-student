import pickle


def load_model(model_path):
    """
    Load the pickled model from the specified path.

    Args:
        model_path (str): Path to the pickle file containing the trained model.

    Returns:
        model: The loaded machine learning model.
    """
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model


def predict(input_data, model_path="src/web_service/local_objects/model.pkl"):
    """
    Make predictions using the loaded model.

    Args:
        input_data (pd.DataFrame or np.array): The input data for which predictions are to be made.
        model_path (str): Path to the pickle file containing the trained model (default: 'src/web_service/local_objects/model.pkl').

    Returns:
        np.array: Predictions made by the model on the input data.
    """
    model = load_model(model_path)
    predictions = model.predict(input_data)
    return predictions
