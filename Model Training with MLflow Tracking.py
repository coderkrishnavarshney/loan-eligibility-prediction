import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from src.data.preprocess import load_and_preprocess_data
from src.models.model_evaluation import evaluate_model
from src.utils.logger import get_logger
import yaml

logger = get_logger(__name__)

def train_and_log_model():
    # Load config
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    # Set up MLflow
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("Loan_Eligibility_Prediction")
    
    # Load and preprocess data
    X_train, X_test, y_train, y_test = load_and_preprocess_data(config)
    
    with mlflow.start_run():
        # Log parameters
        mlflow.log_param("test_size", config["model"]["test_size"])
        mlflow.log_param("random_state", config["model"]["random_state"])
        
        # Hyperparameter tuning
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [5, 10, 15],
            'min_samples_split': [2, 5, 10]
        }
        
        # Model training with GridSearch
        model = GridSearchCV(
            RandomForestClassifier(),
            param_grid,
            cv=5,
            scoring='accuracy',
            n_jobs=-1
        )
        model.fit(X_train, y_train)
        
        # Log best parameters
        mlflow.log_params(model.best_params_)
        
        # Evaluate model
        metrics = evaluate_model(model.best_estimator_, X_test, y_test)
        mlflow.log_metrics(metrics)
        
        # Log model
        mlflow.sklearn.log_model(model.best_estimator_, "model")
        
        # Save model
        import joblib
        joblib.dump(model.best_estimator_, config["model"]["model_path"])
        
        logger.info(f"Model trained and saved with accuracy: {metrics['accuracy']}")
    
    return model.best_estimator_