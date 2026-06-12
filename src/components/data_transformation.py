import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)

from src.constants import TARGET_COLUMN
from src.utils.common import save_object
from src.logger import logging

#class DataTransformation:
class DataTransformation:

    def __init__(self, config):
        self.config = config

    # Preprocessor Method
    def get_data_transformer_object(self):

        numerical_columns = [
            "Age",
            "Attendance",
            "Study_Hours",
            "Assignments_Completed",
            "Previous_Grades"
        ]

        categorical_columns = [
            "Gender",
            "Participation",
            "Internet_Access",
            "Family_Support"
        ]
    # Numerical Pipeline
        num_pipeline = Pipeline(
            steps=[
                (
                    "scaler",
                    StandardScaler()
                )
            ]
        )
    # Categorical Pipeline
        cat_pipeline = Pipeline(
            steps=[
                (
                    "encoder",
                    OneHotEncoder(
                        handle_unknown="ignore"
                    )
                )
            ]
        )
    # Column Transformer
        preprocessor = ColumnTransformer(
            transformers=[
                (
                    "num",
                    num_pipeline,
                    numerical_columns
                ),
                (
                    "cat",
                    cat_pipeline,
                    categorical_columns
                )
            ]
        )

        return preprocessor
    
    def initiate_data_transformation(self, train_path, test_path):

        logging.info("Reading train and test datasets")

        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        #split features and target
        X_train = train_df.drop( columns=[TARGET_COLUMN])

        y_train = train_df[TARGET_COLUMN]

        X_test = test_df.drop( columns=[TARGET_COLUMN])

        y_test = test_df[TARGET_COLUMN]


        #get preprocessor object
        logging.info("Obtaining preprocessing object") 

        preprocessor = (self.get_data_transformer_object())

        #fit and transform train data
        logging.info("Applying preprocessing transformations")

        X_train_transformed = (preprocessor.fit_transform( X_train))
        X_test_transformed = (preprocessor.transform( X_test))

        #save preprocessor object
        logging.info("Saving preprocessing object")

        save_object( self.config.preprocessor_obj_file_path, preprocessor)

        return (
           X_train_transformed,
           y_train.values,
           X_test_transformed,
           y_test.values,
           self.config.preprocessor_obj_file_path
       )
        