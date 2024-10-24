import os
import pickle
from functools import lru_cache

from loguru import logger


@lru_cache
def load_model(filepath: os.PathLike):
    """Load model from local_objects."""
    logger.info(f"Loading model from {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)
