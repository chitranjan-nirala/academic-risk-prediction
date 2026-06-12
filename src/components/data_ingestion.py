import os
import pandas as pd

from sklearn.model_selection import train_test_split

from src.logger import logging
from src.constants import (
    TARGET_COLUMN,
    TEST_SIZE,
    RANDOM_STATE
)


class DataIngestion:

    def __init__(self, config):
        self.config = config

    def initiate_data_ingestion(self):

        logging.info("Reading dataset")

        df = pd.read_csv(
            self.config.raw_data_path
        )

        logging.info(
            f"Dataset Shape: {df.shape}"
        )

        logging.info(
            f"Columns: {df.columns.tolist()}"
        )

        # Verify target exists
        if TARGET_COLUMN not in df.columns:
            raise ValueError(
                f"{TARGET_COLUMN} column not found in dataset"
            )

        # Drop leakage columns
        df = df.drop(
            columns=[
                "Student_ID",
                "Exam_Score"
            ]
        )

        logging.info(
            f"Shape after dropping leakage columns: {df.shape}"
        )

        train_set, test_set = train_test_split(
            df,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
            stratify=df[TARGET_COLUMN]
        )

        os.makedirs("artifacts", exist_ok=True)

        train_set.to_csv(
            self.config.train_data_path,
            index=False
        )

        test_set.to_csv(
            self.config.test_data_path,
            index=False
        )

        logging.info(
            f"Train Shape: {train_set.shape}"
        )

        logging.info(
            f"Test Shape: {test_set.shape}"
        )

        logging.info(
            "Train and Test files saved successfully"
        )

        return (
            self.config.train_data_path,
            self.config.test_data_path
        )