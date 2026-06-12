import pickle

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def evaluate_models(
    X_train,
    y_train,
    X_test,
    y_test,
    models
):

    report = {}

    for model_name, model in models.items():

        model.fit(
            X_train,
            y_train
        )

        y_pred = model.predict(
            X_test
        )

        report[model_name] = {
            "accuracy": accuracy_score(
                y_test,
                y_pred
            ),
            "precision": precision_score(
                y_test,
                y_pred
            ),
            "recall": recall_score(
                y_test,
                y_pred
            ),
            "f1_score": f1_score(
                y_test,
                y_pred
            )
        }

    return report


def save_object(file_path, obj):

    with open(file_path, "wb") as file_obj:
        pickle.dump(obj, file_obj)


def load_object(file_path):

    with open(file_path, "rb") as file_obj:
        return pickle.load(file_obj)