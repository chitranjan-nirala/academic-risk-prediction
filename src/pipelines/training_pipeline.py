from src.config.configuration import (
    ConfigurationManager
)

from src.components.data_ingestion import (
    DataIngestion
)

from src.components.data_transformation import (
    DataTransformation
)

from src.components.model_trainer import (
    ModelTrainer
)

from src.components.model_evaluation import (
    ModelEvaluation
)

if __name__ == "__main__":

    config = ConfigurationManager()
    # -------------------------
    # Data Ingestion
    # -------------------------
    ingestion_config = (
        config.get_data_ingestion_config()
    )

    ingestion = DataIngestion(
        ingestion_config
    )

    train_path, test_path = (
        ingestion.initiate_data_ingestion()
    )

    # -------------------------
    # Data Transformation
    # -------------------------
    transformation_config = (
        config.get_data_transformation_config()
    )

    transformation = DataTransformation(
        transformation_config
    )

    (
    X_train,
    y_train,
    X_test,
    y_test,
    preprocessor_path
    ) = transformation.initiate_data_transformation(
    train_path,
    test_path
   )

    # -------------------------
    # Model Training
    # -------------------------
    model_trainer_config = (
    config.get_model_trainer_config()
    )
   
   #create model trainer object
    model_trainer = ModelTrainer(
    model_trainer_config
   )
    
    #train model and evaluate
    results = model_trainer.initiate_model_trainer(
    X_train,
    y_train,
    X_test,
    y_test
    )

    print(results) 


    # -------------------------
    # Model evaluation
    # -------------------------
    evaluator = ModelEvaluation()

    report = (
    evaluator.initiate_model_evaluation(
        X_train,
        y_train,
        X_test,
        y_test
        )
    )

    print(report)
    import json

with open("artifacts/metrics.json", "w") as f:
    json.dump(report, f, indent=4)