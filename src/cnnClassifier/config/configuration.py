import yaml
from src.entity.entity import (
    DataIngestionConfig,
    DataPreprocessingConfig,
    ModelTrainingConfig,
    ModelEvaluationConfig,
    PredictionConfig
)

class ConfigurationManager:
    def __init__(self, config_path="config/config.yaml", params_path="params.yaml"):
        self.config = self.read_yaml(config_path)
        self.params = self.read_yaml(params_path)

    def read_yaml(self, file_path):
        """Reads a YAML file and returns its content as a dictionary."""
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def get_data_ingestion_config(self):
        """Returns Data Ingestion Configuration."""
        return DataIngestionConfig(**self.config["data_ingestion"])

    def get_data_preprocessing_config(self):
        """Returns Data Preprocessing Configuration."""
        return DataPreprocessingConfig(**self.config["data_preprocessing"])

    def get_model_training_config(self):
        """Returns Model Training Configuration."""
        return ModelTrainingConfig(
            **self.config["model_training"],
            learning_rate=self.params["learning_rate"]
        )

    def get_model_evaluation_config(self):
        """Returns Model Evaluation Configuration."""
        return ModelEvaluationConfig(**self.config["model_evaluation"])

    def get_prediction_config(self):
        """Returns Prediction Configuration."""
        return PredictionConfig(**self.config["prediction"])
