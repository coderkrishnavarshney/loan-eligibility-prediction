import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class LoanFeatureEngineer(BaseEstimator, TransformerMixin):
    """Custom feature engineering for loan prediction"""
    
    def __init__(self):
        self.feature_names = []
        
    def fit(self, X, y=None):
        return self
        
    def transform(self, X):
        # Create total income feature
        X['TotalIncome'] = X['ApplicantIncome'] + X['CoapplicantIncome']
        
        # Create EMI feature (LoanAmount in thousands)
        X['EMI'] = X['LoanAmount'] / X['Loan_Amount_Term']
        
        # Create income to loan ratio
        X['IncomeToLoanRatio'] = X['TotalIncome'] / (X['LoanAmount'] + 1e-6)
        
        # Create credit score bins
        X['CreditScoreBin'] = pd.cut(
            X['Credit_History'],
            bins=[-1, 0.5, 1],
            labels=['Poor', 'Good']
        )
        
        # One-hot encode new categorical features
        X = pd.get_dummies(X, columns=['CreditScoreBin'], drop_first=True)
        
        self.feature_names = X.columns.tolist()
        return X
    
    def get_feature_names(self):
        return self.feature_names