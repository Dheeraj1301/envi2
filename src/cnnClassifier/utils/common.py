import os
import yaml
import json
import shutil
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

def read_yaml(file_path):
    """Reads a YAML file and returns the content as a dictionary."""
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
        return None

def write_yaml(file_path, data):
    """Writes a dictionary to a YAML file."""
    try:
        with open(file_path, "w") as file:
            yaml.dump(data, file)
    except Exception as e:
        logging.error(f"Error writing {file_path}: {e}")

def read_json(file_path):
    """Reads a JSON file and returns the content as a dictionary."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
        return None

def write_json(file_path, data):
    """Writes a dictionary to a JSON file."""
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f"Error writing {file_path}: {e}")

def create_directories(paths):
    """Creates multiple directories if they don't exist."""
    for path in paths:
        try:
            os.makedirs(path, exist_ok=True)
            logging.info(f"Directory created: {path}")
        except Exception as e:
            logging.error(f"Error creating directory {path}: {e}")

def delete_directory(path):
    """Deletes a directory if it exists."""
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
            logging.info(f"Deleted directory: {path}")
    except Exception as e:
        logging.error(f"Error deleting {path}: {e}")

def get_file_size(file_path):
    """Returns the file size in KB."""
    try:
        size = os.path.getsize(file_path) / 1024  # Convert to KB
        return round(size, 2)
    except Exception as e:
        logging.error(f"Error getting file size for {file_path}: {e}")
        return None
