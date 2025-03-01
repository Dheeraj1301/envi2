
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import gdown
import zipfile
from src.config.configuration import ConfigurationManager
from src.utils.common import create_directories
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

class DataIngestion:
    def __init__(self, config):
        self.config = config
        create_directories([self.config.root_dir])

    def download_data(self):
        """Downloads the dataset from the provided URL."""
        if not os.path.exists(self.config.local_data_file):
            logging.info(f"Downloading data from {self.config.source_URL}...")
            gdown.download(self.config.source_URL, self.config.local_data_file, quiet=False)
            logging.info("Download complete!")
        else:
            logging.info("Data file already exists. Skipping download.")

    def extract_data(self):
        """Extracts the downloaded ZIP file."""
        if not os.path.exists(self.config.unzip_dir):
            logging.info("Extracting data...")
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
            logging.info("Extraction complete!")
        else:
            logging.info("Data already extracted. Skipping extraction.")

    def initiate_data_ingestion(self):
        """Runs the full data ingestion process."""
        self.download_data()
        self.extract_data()

if __name__ == "__main__":
    config_manager = ConfigurationManager()
    ingestion_config = config_manager.get_data_ingestion_config()
    data_ingestion = DataIngestion(ingestion_config)
    data_ingestion.initiate_data_ingestion()
