import numpy as np
import json
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from src.utils.common import save_object
from src.logger import logging

#class ModelTrainer:
class ModelTrainer:

    def __init__(self, config):
        self.config = config

    def initiate_model_trainer(self,
        X_train,
        y_train,
        X_test,
        y_test
    ):    
        model = LogisticRegression( max_iter=1000)

        model.fit(X_train, y_train)    

        y_pred = model.predict(X_test)

        y_prob = model.predict_proba(X_test)[:,1]

    #evaluation metrics
        accuracy = accuracy_score(
            y_test,
            y_pred
        )
        logging.info(f"Accuracy: {accuracy}")

        precision = precision_score(
            y_test,
            y_pred
        )
        logging.info(f"Precision: {precision}")

        recall = recall_score(
            y_test,
            y_pred
        )
        logging.info(f"Recall: {recall}")
        f1 = f1_score(
            y_test,
            y_pred
        )
        logging.info(f"F1 Score: {f1}")
        
        roc_auc = roc_auc_score(
            y_test,
            y_prob
        )

        logging.info(f"ROC AUC: {roc_auc}")

        #save model
        logging.info("Saving Model")
        save_object(
           self.config.trained_model_file_path,
           model
        )
        
        metrics = {
            "accuracy": float(accuracy),
            "precision": float(precision),
            "recall": float(recall),
            "f1_score": float(f1),
            "roc_auc": float(roc_auc)
        }

        with open("artifacts/metrics.json", "w") as f:

         json.dump(metrics, f, indent=4 )

        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "roc_auc": roc_auc
       }