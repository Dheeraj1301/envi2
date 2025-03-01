from src.pipeline.train_pipeline import train_pipeline
from src.pipeline.predict_pipeline import predict_pipeline
import argparse
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))


logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

def main():
    parser = argparse.ArgumentParser(description="Run the COVID-19 severity prediction pipeline.")
    parser.add_argument("--train", action="store_true", help="Run the training pipeline.")
    parser.add_argument("--predict", action="store_true", help="Run the prediction pipeline.")

    args = parser.parse_args()

    if args.train:
        logging.info("Executing training pipeline...")
        train_pipeline()

    if args.predict:
        logging.info("Executing prediction pipeline...")
        predict_pipeline()

if __name__ == "__main__":
    main()
