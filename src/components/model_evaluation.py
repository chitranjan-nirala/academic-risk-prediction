from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    auc
)

import matplotlib.pyplot as plt
import os

from src.utils.common import evaluate_models


class ModelEvaluation:

    def __init__(self):
        pass

    def initiate_model_evaluation(
        self,
        X_train,
        y_train,
        X_test,
        y_test
    ):

        models = {

            "Logistic Regression":
            LogisticRegression(
                max_iter=1000
            ),

            "Random Forest":
            RandomForestClassifier(
                n_estimators=100,
                random_state=42
            ),

            "Gradient Boosting":
            GradientBoostingClassifier(
                random_state=42
            )
        }

        report = evaluate_models(
            X_train,
            y_train,
            X_test,
            y_test,
            models
        )

        # ==================================
        # Train Logistic Regression
        # ==================================

        model = LogisticRegression(
            max_iter=1000
        )

        model.fit(
            X_train,
            y_train
        )

        y_pred = model.predict(X_test)

        y_prob = model.predict_proba(X_test)[:, 1]

        os.makedirs("artifacts", exist_ok=True)

        # ==================================
        # CONFUSION MATRIX
        # ==================================

        cm = confusion_matrix(
            y_test,
            y_pred
        )

        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm
        )

        disp.plot()

        plt.savefig(
            "artifacts/confusion_matrix.png",
            bbox_inches="tight"
        )

        plt.close()

        # ==================================
        # ROC CURVE
        # ==================================

        fpr, tpr, _ = roc_curve(
            y_test,
            y_prob
        )

        roc_auc = auc(
            fpr,
            tpr
        )

        plt.figure(figsize=(6, 5))

        plt.plot(
            fpr,
            tpr,
            label=f"AUC = {roc_auc:.3f}"
        )

        plt.plot(
            [0, 1],
            [0, 1],
            linestyle="--"
        )

        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC Curve")
        plt.legend()

        plt.savefig(
            "artifacts/roc_curve.png",
            bbox_inches="tight"
        )

        plt.close()

        return report