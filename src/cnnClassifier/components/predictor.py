import tensorflow as tf
import numpy as np
import cv2
import json
from src.config.configuration import ConfigurationManager
from src.utils.common import write_json
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

class Predictor:
    def __init__(self, config):
        self.config = config
        logging.info("Loading trained model...")
        self.model = tf.keras.models.load_model(self.config.model_path)

    def preprocess_image(self, image_path):
        """Loads and preprocesses a single image."""
        logging.info(f"Processing image: {image_path}")
        image = cv2.imread(image_path)
        image = cv2.resize(image, self.config.image_size)
        image = image / 255.0  # Normalize
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        return image

    def predict(self):
        """Predicts the severity percentage for a new image."""
        image = self.preprocess_image(self.config.input_image_path)
        prediction = self.model.predict(image)[0][0]
        severity_percentage = round(float(prediction) * 100, 2)

        result = {
            "input_image": self.config.input_image_path,
            "severity_percentage": severity_percentage
        }
        logging.info(f"Prediction result: {result}")

        write_json(self.config.output_result_path, result)
        return result

if __name__ == "__main__":
    config_manager = ConfigurationManager()
    prediction_config = config_manager.get_prediction_config()
    predictor = Predictor(prediction_config)
    predictor.predict()
