import pandas as pd


class AnalyticsEngine:

    def generate_summary(self, df):

        total_predictions = len(df)

        high_risk = len(
            df[df["risk_probability"] >= 70]
        )

        medium_risk = len(
            df[
                (df["risk_probability"] >= 40)
                &
                (df["risk_probability"] < 70)
            ]
        )

        low_risk = len(
            df[df["risk_probability"] < 40]
        )

        avg_risk = round(
            df["risk_probability"].mean(),
            2
        )

        return {
            "total_predictions": total_predictions,
            "high_risk": high_risk,
            "medium_risk": medium_risk,
            "low_risk": low_risk,
            "average_risk": avg_risk
        }