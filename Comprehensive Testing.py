import pytest
import pandas as pd
from src.data.preprocess import load_and_preprocess_data
from src.utils.helpers import load_config

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'Gender': ['Male', 'Female', 'Male'],
        'Married': ['Yes', 'No', 'Yes'],
        'LoanAmount': [100, 200, None],
        'Credit_History': [1.0, None, 0.0],
        'Loan_Status': ['Y', 'N', 'Y']
    })

def test_missing_value_handling(sample_data):
    config = load_config()
    X_train, _, _, _ = load_and_preprocess_data(config, sample_data)
    
    # Check if missing values are filled
    assert X_train['LoanAmount'].isna().sum() == 0
    assert X_train['Credit_History'].isna().sum() == 0

def test_categorical_encoding(sample_data):
    config = load_config()
    X_train, _, _, _ = load_and_preprocess_data(config, sample_data)
    
    # Check if categorical columns are encoded
    assert set(X_train['Gender'].unique()).issubset({0, 1})
    assert set(X_train['Married'].unique()).issubset({0, 1})