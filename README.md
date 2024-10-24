<div align="center">

# xhec-mlops-project-student

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-student/blob/main/.pre-commit-config.yaml)

</div>

This repository has for purpose to industrialize the [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) Kaggle contest.

<details>
<summary>Details on the Abalone Dataset</summary>

The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.

**Goal**: predict the age of abalone (column "Rings") from physical measurements ("Shell weight", "Diameter", etc...)

You can download the dataset on the [Kaggle page](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset)

</details>

## Setup

### Python version

- Supported version : <strong>3.10</strong> <br>

Please make sure you have this version installed to be able to run the app on your machine.

### Create a virtual environment

To contribute to or run the app, you will need to use a virtual environment.

If you have a Miniconda installed:

```
# Create env
$ cd <this repository>
$ conda env create --file environment.yml

# Activate your environment:
$ conda activate envname

# Check python:
(envname) $ which python # Unix
(envname) $ where python # Windows

# In order to stop using this virtual environment:
(envname) $ deactivate
```

Or with virtualenv:

```
# Install virtualenv package
$ pip install virtualenv

# Create the virtual environment
$ virtualenv venv --python=python3.10

# Activate it
$ source venv/Scripts/activate  # Windows
$ source venv/bin/activate  # Unix
```

### Handle dependencies

You need to install all the dependencies in order to be able to run the app.

#### Virtualenv

With virtualenv, there is two files: `requirements.txt` that contains dependencies to run the app (which you need to install either way), and `requirements-dev.txt` with dependencies to dev on the app (not required if you only plan to run the app).

```
$ source venv/bin/activate  # Activate env
(venv) $ pip install -r requirements.txt
```

Or if you want to contribute:

```
$ source venv/bin/activate  # Activate env
(venv) $ pip install -r requirements.txt
(venv) $ pip install -r requirements-dev.txt
```

If you need to amend the dependencies of the project, then don't forget to add them to the `requirements.in` and/or `requirements-dev.in` files before.

#### Conda

If the name is correctly specified in the `environment.yml` file, then there is no need to run the following command from within the virtual environment:

```
conda env update --file environment.yml --prune
```

If you need to amend the dependencies of the project, then simply run:

```
$ conda activate envname  # Activate env
(envname) $ conda install -c <library>
```

You should not forget to add this new dependence to `environment.yml`.

### Before contributing

Run:

```bash
pre-commit install
```

## Model Training with Prefect and MLFlow

### Prerequisites

1. Start the Prefect server in a terminal:
```bash
prefect server start
```
You can access the Prefect UI at http://localhost:4200

2. Start an MLFlow server in another terminal:
```bash
mlflow server
```
You can access the MLflow UI at http://127.0.0.1:5000

### Training the Model

#### Single Training Run
To train the model once and generate the pickle file, run from the root folder:
```bash
python src/modelling/main.py data/abalone.csv
```
This will:
- Read the abalone dataset
- Preprocess the data
- Train a linear regression model
- Save the model as a pickle file in `src/web_service/local_objects/model.pkl`

You can monitor the training progress in the Prefect UI.

#### Setting Up Automated Retraining
To create a deployment that will automatically retrain the model weekly:
```bash
python src/modelling/main.py data/abalone.csv --create-deployment
```
This will create a scheduled deployment that runs every Sunday at midnight.

### Monitoring

In the Prefect UI (http://localhost:4200), you can:
- View all flow runs and their status
- Monitor task execution
- Access logs and error messages
- Manage deployments and schedules

The training pipeline consists of the following tasks:
1. `read_data`: Loads the abalone dataset
2. `preprocess_data`: Prepares the data for training
3. `train_model`: Trains the linear regression model
4. `save_model`: Saves the trained model as a pickle file```

## Running with Docker

1. **Building the Docker image**

   To build the Docker image for this project, run the following command from the root directory of the project (where the Dockerfile is located):

   ```bash
   docker build -f Dockerfile.app -t abalone-prediction-app .

   ```
2. **Running the Docker container**

   To run the app inside a Docker container, use the following command:

   ```bash
   docker run -d -p 0.0.0.0:8000:8001 -p 0.0.0.0:4200:4201 --name abalone-prediction abalone-prediction-app
   ```

## Using the API

### 1. Health Check

You can verify that the API is running with:

```bash
curl http://localhost:8000/
```

Here is the expected response:
```json
{
    "health_check": "OK",
    "model_version": "1.0.0"
}
```

### 2. Making Predictions

You can predict the age of an abalone based on its physical measurements:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "length": 0.455,
    "diameter": 0.365,
    "height": 0.095,
    "wholeweight": 0.514,
    "shuckedweight": 0.2245,
    "visceraweight": 0.101,
    "shellweight": 0.15
  }'
```

For that specific answer, here is the expected response:
```json
{
    "age": 10
}
```

### Input Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| length | float | Length in mm |
| diameter | float | Diameter in mm |
| height | float | Height in mm |
| wholeweight | float | Whole weight in grams |
| shuckedweight | float | Shucked weight in grams |
| visceraweight | float | Viscera weight in grams |
| shellweight | float | Shell weight in grams |

## Participants

- **JAUNEAU Thibault** - [thibault.jauneau@hec.edu](mailto:thibault.jauneau@hec.edu)
- **NGUYEN Thanh Liêm** - [thanh-liem.nguyen.2023@polytechnique.edu](mailto:thanh-liem.nguyen.2023@polytechnique.edu)
- **ATLASSI-DOUCH Zakaria** - [zakaria.atlassi-douch@hec.edu](mailto:zakaria.atlassi-douch@hec.edu)
- **BENSEDDIQ Safwane** - [safwane-bsd@hotmail.fr](mailto:safwane-bsd@hotmail.fr)
- **JABRI Farah** - [fafou.bouchou@gmail.com](mailto:fafou.bouchou@gmail.com)
