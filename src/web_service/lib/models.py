from pydantic import BaseModel


class InputData(BaseModel):
    """InputData class for predictions."""

    length: float
    diameter: float
    height: float
    wholeweight: float
    shuckedweight: float
    visceraweight: float
    shellweight: float


class PredictionOut(BaseModel):
    """Prediction output class for predictions."""

    age: float
