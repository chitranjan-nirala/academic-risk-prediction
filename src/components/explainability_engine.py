import shap
import pandas as pd


class ExplainabilityEngine:

    def __init__(self, model):

        self.model = model

        self.explainer = shap.Explainer(
            self.model
        )

    def explain(self, data):

        shap_values = self.explainer(
            data
        )

        return shap_values