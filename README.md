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

## Model Training with Prefect

### Prerequisites

1. Start the Prefect server in a terminal:
```bash
prefect server start
```
You can access the Prefect UI at http://localhost:4200

2. Start a Prefect worker in another terminal:
```bash
prefect worker start -p default-agent-pool
```

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

### Running with Docker

1. **Building the Docker image**

   To build the Docker image for this project, run the following command from the root directory of the project (where the Dockerfile is located):

   ```bash
   docker build -f Dockerfile.app .

2. **Running the Docker container**

   To run the app inside a Docker container, use the following command:

   ```bash
   docker run -d -p 8000:8000 --name abalone-prediction abalone-prediction-app




## Table of Contents

- [xhec-mlops-project-student](#xhec-mlops-project-student)
  - [Table of Contents](#table-of-contents)
  - [Deliverables and Evaluation](#deliverables-and-evaluation)
    - [Deliverables](#deliverables)
    - [Evaluation](#evaluation)
  - [Steps to reproduce to build the deliverable](#steps-to-reproduce-to-build-the-deliverable)
    - [Pull requests in this project](#pull-requests-in-this-project)
    - [Tips to work on this project](#tips-to-work-on-this-project)

## Deliverables and notation

### Deliverables

The deliverable of this project is a copy of this repository with the industrialization of the Abalone age prediction model. We expect to see:

1. a workflow to train a model using Prefect

- The workflows to train the model and to make the inference (prediction of the age of abalone) are in separate modules and use Prefect `flow` and `task` objects
- The code to get the trained model and encoder is in a separate module and must be reproducible (not necessarily in a docker container)

2. a Prefect deployment to retrain the model regularly
3. an API that runs on a local app and that allows users to make predictions on new data

- A working API which can be used to make predictions on new data
  - The API can run on a docker container
  - The API has validation on input data (use Pydantic)

### Evaluation

Each of your pull requests will be graded based on the following criteria:

- **Clarity** and quality of code
  - good module structure
  - naming conventions
  - use of docstrings and type hinting
- **Formatting**

  - respect of clear code conventions

  _P.S. you can use a linter and automatic code formatters to help you with that_

- Proper **Functioning** of the code
  - the code must run without bugs

Bseides the evaluation of the pull requests, we will also evaluate:

- **Reproducibility** and clarity of instructions to run the code (we will actually try to run your code)
  - Having a clear README.md with
    - the context of the project
    - the name of the participants and their github users
    - the steps to recreate the Python environment
    - the instructions to run all parts of the code
- Use of _Pull Requests_ (see below) to coordinate your collaboration

## Steps to reproduce to build the deliverable

To help you with the structure and order of steps to perform in this project, we created different pull requests templates.
Each branch in this repository corresponds to a future pull request and has an attached markdown file with the instructions to perform the tasks of the pull request.
Each branch starts with a number.
You can follow the order of the branches to build your project and collaborate.

> [!NOTE]
> There are "TODO" in the code of the different branches. Each "TODO" corresponds to a task to perform to build the project.
> [!IMPORTANT]
> Remember to remove all code that is not used before the end of the project (including all TODO tags in the code).

**Please follow these steps**:

- If not done already, create a GitHub account
- If not done already, create a [Kaggle account](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F) (so you can download the dataset)
- Fork this repository (one person per group)

**WARNING**: make sure to **unselect** the option "Copy the `master` branch only", so you have all the branches in the forked repository.

- Add the different members of your group as admin to your forked repository
- Follow the order of the numbered branches and for each branch:
  - Read the PR_i.md (where i is the number of the branch) file to understand the task to perform
    > [!NOTE]
    > Dont forget to integrate your work from past branches (except for when working on branch #1 obviously (!))
    >
    > ```bash
    > git checkout branch_number_i
    > git pull origin master
    > # At this point, you might have a VIM window opening, you can close it using the command ":wq"
    > git push
    > ```
    - Read and **follow** all the instructions in the the PR instructions file
    - Do as many commits as necessary on the branch_number_i to perform the task indicated in the corresponding markdown file
    - Open **A SINGLE** pull request from this branch to the main branch of your forked repository
    - Once done, merge the pull request in the main branch of your forked repository

### Pull requests in this project

Github [Pull Requests](https://docs.github.com/articles/about-pull-requests) are a way to propose changes to a repository. They have for purpose to integrate the work of _feature branches_ into the main branch of the repository, with a collaborative review process.

**PR tips:**

Make sure that you select your own repository when selecting the base repository:

![PR Wrong](assets/PR_wrong.png)

It should rather look like this:

![PR Right](assets/PR_right.png)

### Tips to work on this project

- Use a virtual environment to install the dependencies of the project (conda or virtualenv for instance)

- Once your virtual environment is activated, install pre-commit hooks to automatically format your code before each commit:

```bash
pip install pre-commit
pre-commit install
```

This will guarantee that your code is formatted correctly and of good quality before each commit.

- Use a `requirements.in` file to list the dependencies of your project. You can use the following command to generate a `requirements.txt` file from a `requirements.in` file:

```bash
pip-compile requirements.in
```
