import pickle


def pickle_object(obj, file_path):
    """
    Pickle and save the given object to the specified file path.

    Args:
        obj: The object to be pickled.
        file_path (str): The path where the pickled object will be saved.
    """
    with open(file_path, "wb") as f:
        pickle.dump(obj, f)
