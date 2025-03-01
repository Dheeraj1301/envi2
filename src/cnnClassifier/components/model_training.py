import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from src.config.configuration import ConfigurationManager
from src.utils.common import create_directories
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

class ModelTraining:
    def __init__(self, config):
        self.config = config
        create_directories([self.config.root_dir])

    def build_model(self):
        """Creates a CNN model architecture."""
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(*self.config.image_size, 3)),
            MaxPooling2D(2, 2),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D(2, 2),
            Flatten(),
            Dense(128, activation='relu'),
            Dropout(0.5),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=self.config.learning_rate),
                      loss="binary_crossentropy",
                      metrics=["accuracy"])
        return model

    def train_model(self, train_data):
        """Trains the CNN model."""
        logging.info("Building model...")
        model = self.build_model()
        
        logging.info("Starting training...")
        model.fit(train_data, epochs=self.config.epochs)
        
        logging.info(f"Saving model to {self.config.model_path}...")
        model.save(self.config.model_path)
        
        logging.info("Model training complete!")

if __name__ == "__main__":
    config_manager = ConfigurationManager()
    training_config = config_manager.get_model_training_config()
    model_trainer = ModelTraining(training_config)

    # Load preprocessed data
    preprocess_config = config_manager.get_data_preprocessing_config()
    from src.components.data_preprocessing import DataPreprocessing
    data_preprocessor = DataPreprocessing(preprocess_config)
    processed_data = data_preprocessor.initiate_data_preprocessing()

    # Train model
    model_trainer.train_model(processed_data)
