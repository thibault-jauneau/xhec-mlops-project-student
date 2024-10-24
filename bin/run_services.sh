#!/bin/bash

mlflow ui --host 0.0.0.0 --port 5000 &
prefect server start --host 0.0.0.0 --port 4201 &
uvicorn main:app --host 0.0.0.0 --port 8001
