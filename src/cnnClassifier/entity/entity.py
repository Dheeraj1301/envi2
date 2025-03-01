from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: str
    source_URL: str
    local_data_file: str
    unzip_dir: str

@dataclass
class DataPreprocessingConfig:
    root_dir: str
    processed_data_file: str
    image_size: tuple

@dataclass
class ModelTrainingConfig:
    root_dir: str
    model_path: str
    epochs: int
    batch_size: int
    image_size: tuple
    learning_rate: float

@dataclass
class ModelEvaluationConfig:
    root_dir: str
    model_path: str
    test_data_path: str
    metrics_file: str

@dataclass
class PredictionConfig:
    model_path: str
    input_image_path: str
    output_result_path: str
