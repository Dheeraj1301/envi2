import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import DataPreprocessing
from src.components.model_training import ModelTraining
from src.config.configuration import ConfigurationManager
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

def train_pipeline():
    """Runs the entire training pipeline step by step."""
    config_manager = ConfigurationManager()

    # Data Ingestion
    logging.info("Starting data ingestion...")
    ingestion_config = config_manager.get_data_ingestion_config()
    data_ingestion = DataIngestion(ingestion_config)
    data_ingestion.initiate_data_ingestion()
    logging.info("Data ingestion completed!")

    # Data Preprocessing
    logging.info("Starting data preprocessing...")
    preprocess_config = config_manager.get_data_preprocessing_config()
    data_preprocessor = DataPreprocessing(preprocess_config)
    train_data = data_preprocessor.initiate_data_preprocessing()
    logging.info("Data preprocessing completed!")

    # Model Training
    logging.info("Starting model training...")
    training_config = config_manager.get_model_training_config()
    model_trainer = ModelTraining(training_config)
    model_trainer.train_model(train_data)
    logging.info("Model training completed!")

if __name__ == "__main__":
    train_pipeline()

