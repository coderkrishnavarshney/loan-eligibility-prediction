# Loan Eligibility Prediction System

[![CI/CD Pipeline](https://github.com/yourusername/loan-eligibility-prediction/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/yourusername/loan-eligibility-prediction/actions/workflows/ci-cd.yml)
[![codecov](https://codecov.io/gh/yourusername/loan-eligibility-prediction/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/loan-eligibility-prediction)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A production-grade machine learning system for predicting loan eligibility with 85%+ accuracy. Designed to meet FAANG engineering standards.

## Features

- **ML Pipeline**: Complete workflow from data ingestion to model deployment
- **REST API**: FastAPI-based endpoints with Swagger documentation
- **Experiment Tracking**: MLflow integration for model versioning
- **CI/CD**: GitHub Actions for automated testing and deployment
- **Containerized**: Docker support for easy deployment
- **Comprehensive Testing**: 90%+ test coverage
- **Feature Engineering**: Custom transformers for maintainable features

## Installation

### Prerequisites

- Python 3.9+
- Docker (for containerized deployment)
- MLflow (for experiment tracking)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/loan-eligibility-prediction.git
   cd loan-eligibility-prediction
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Set up pre-commit hooks:
   ```bash
   pre-commit install


### Usage
1. Training the Model:
   ```bash
   python -m src.models.train_model
2. Running the API:
   ```bash
   uvicorn src.api.app:app --reload

   
### Docker Deployment
1. Build the image:
   ```bash
   docker build -t loan-prediction-api .
3. Run the container:
   ```bash
   docker run -p 8000:8000 loan-prediction-api

### Making Predictions
1. Making Predictions:
   ```bash
   curl -X 'POST' \
  'http://localhost:8000/api/v1/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Gender": "Male",
  "Married": "Yes",
  "Dependents": "0",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 2000,
  "LoanAmount": 150,
  "Loan_Amount_Term": 360,
  "Credit_History": 1.0,
  "Property_Area": "Urban"
}'
### Project Structure
1. ```text
   ├── .github/            # GitHub Actions workflows
├── config/            # Configuration files
├── data/              # Data storage
├── docs/              # Documentation
├── models/            # Trained models and experiments
├── notebooks/         # Jupyter notebooks for exploration
├── src/               # Source code
├── tests/             # Test suites
├── Dockerfile         # Container configuration
├── Makefile           # Development commands
├── pyproject.toml     # Project metadata
├── requirements.txt   # Python dependencies
└── README.md          # This file

### Testing
### Contributing
### License
### Contact
### Key Features of This Documentation
