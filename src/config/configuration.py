import os

from src.entity.config_entity import (
    DataIngestionConfig,
    DataTransformationConfig,ModelTrainerConfig
)


class ConfigurationManager:

    def get_data_ingestion_config(self):

        return DataIngestionConfig(
            train_data_path=os.path.join(
                "artifacts",
                "train.csv"
            ),
            test_data_path=os.path.join(
                "artifacts",
                "test.csv"
            ),
            raw_data_path=os.path.join(
                "data",
                "raw",
                "student_performance.csv"
            )
        )

    def get_data_transformation_config(self):

        return DataTransformationConfig(
            preprocessor_obj_file_path=os.path.join(
                "artifacts",
                "preprocessor.pkl"
            )
        )
    
    def get_model_trainer_config(self):

        return ModelTrainerConfig(
        trained_model_file_path=
        "artifacts/model.pkl"
        )