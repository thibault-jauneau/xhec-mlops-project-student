# Use this module to code a `pickle_object` function. This will be useful to pickle the model (and encoder if need be).
import pickle

def pickle_object(obj, file_path):
    """Pickle the given object to the specified file path."""
    with open(file_path, "wb") as f:
        pickle.dump(obj, f)
