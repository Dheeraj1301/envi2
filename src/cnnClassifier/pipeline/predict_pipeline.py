from src.components.predictor import Predictor
from src.config.configuration import ConfigurationManager
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

def predict_pipeline():
    """Runs the prediction pipeline for a single image."""
    config_manager = ConfigurationManager()

    logging.info("Starting prediction process...")
    prediction_config = config_manager.get_prediction_config()
    predictor = Predictor(prediction_config)

    # Run prediction
    result = predictor.predict()
    
    logging.info(f"Prediction completed: {result}")

if __name__ == "__main__":
    predict_pipeline()
