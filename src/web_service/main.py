from app_config import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    MODEL_VERSION,
    PATH_TO_MODEL,
)
from fastapi import FastAPI
from lib.inference import run_inference
from lib.models import InputData, PredictionOut
from lib.utils import load_model

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION)


@app.get("/")
def home() -> dict:
    """Home page."""
    return {"health_check": "OK", "model_version": MODEL_VERSION}


@app.post("/predict", response_model=PredictionOut, status_code=201)
def predict(payload: InputData) -> dict:
    """Prediction endpoint."""
    model = load_model(PATH_TO_MODEL)
    y = run_inference([payload], model)
    return {"age": y[0]}
