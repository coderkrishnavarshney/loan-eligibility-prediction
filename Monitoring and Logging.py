import logging
import logging.config
import yaml
import os
from pathlib import Path

def setup_logging():
    """Setup logging configuration"""
    log_config_path = Path(__file__).parent.parent.parent / "config" / "logging.yaml"
    
    if os.path.exists(log_config_path):
        with open(log_config_path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
    
    logger = logging.getLogger(__name__)
    logger.info("Logging configuration set up successfully")
    return logger

def get_logger(name):
    """Get a configured logger instance"""
    return logging.getLogger(name)