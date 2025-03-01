import os

# Define root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for artifacts
ARTIFACTS_DIR = os.path.join(ROOT_DIR, "../../artifacts")
DATA_INGESTION_DIR = os.path.join(ARTIFACTS_DIR, "data_ingestion")
DATA_PREPROCESSING_DIR = os.path.join(ARTIFACTS_DIR, "data_preprocessing")
MODEL_TRAINING_DIR = os.path.join(ARTIFACTS_DIR, "model_training")
MODEL_EVALUATION_DIR = os.path.join(ARTIFACTS_DIR, "model_evaluation")

# File paths
CONFIG_FILE_PATH = "config/config.yaml"
PARAMS_FILE_PATH = "params.yaml"
MODEL_FILE_PATH = os.path.join(MODEL_TRAINING_DIR, "covid_model.h5")
METRICS_FILE_PATH = os.path.join(MODEL_EVALUATION_DIR, "metrics.json")

# Model Parameters
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 20
LEARNING_RATE = 0.001

# Prediction Paths
INPUT_IMAGE_PATH = "artifacts/input/test_image.jpg"
OUTPUT_RESULT_PATH = "artifacts/output/prediction.json"
