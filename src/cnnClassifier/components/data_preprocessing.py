import os
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from src.config.configuration import ConfigurationManager
from src.utils.common import create_directories
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

class DataPreprocessing:
    def __init__(self, config):
        self.config = config
        create_directories([self.config.root_dir])

    def preprocess_images(self, directory):
        """Applies preprocessing transformations to images."""
        datagen = ImageDataGenerator(rescale=1.0 / 255)  # Normalize pixel values
        return datagen.flow_from_directory(
            directory,
            target_size=self.config.image_size,
            batch_size=32,
            class_mode="binary"
        )

    def initiate_data_preprocessing(self):
        """Runs the full data preprocessing pipeline."""
        logging.info("Starting data preprocessing...")
        processed_data = self.preprocess_images(self.config.processed_data_file)
        logging.info("Data preprocessing complete!")
        return processed_data

if __name__ == "__main__":
    config_manager = ConfigurationManager()
    preprocess_config = config_manager.get_data_preprocessing_config()
    data_preprocessor = DataPreprocessing(preprocess_config)
    processed_data = data_preprocessor.initiate_data_preprocessing()
