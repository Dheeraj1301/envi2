import tensorflow as tf
import json
import numpy as np
from src.config.configuration import ConfigurationManager
from src.utils.common import read_yaml, write_json
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

class ModelEvaluation:
    def __init__(self, config):
        self.config = config

    def load_model(self):
        """Loads the trained model from file."""
        logging.info(f"Loading model from {self.config.model_path}...")
        model = tf.keras.models.load_model(self.config.model_path)
        return model

    def evaluate_model(self, test_data):
        """Evaluates the model and saves metrics to a JSON file."""
        model = self.load_model()
        
        logging.info("Evaluating model on test data...")
        loss, accuracy = model.evaluate(test_data)
        
        metrics = {"loss": round(float(loss), 4), "accuracy": round(float(accuracy), 4)}
        
        logging.info(f"Model evaluation results: {metrics}")
        write_json(self.config.metrics_file, metrics)
        return metrics

if __name__ == "__main__":
    config_manager = ConfigurationManager()
    evaluation_config = config_manager.get_model_evaluation_config()
    model_evaluator = ModelEvaluation(evaluation_config)

    # Load test data
    preprocess_config = config_manager.get_data_preprocessing_config()
    from src.components.data_preprocessing import DataPreprocessing
    data_preprocessor = DataPreprocessing(preprocess_config)
    test_data = data_preprocessor.initiate_data_preprocessing()

    # Evaluate the model
    model_evaluator.evaluate_model(test_data)
