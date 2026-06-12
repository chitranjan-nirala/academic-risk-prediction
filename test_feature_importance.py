from src.utils.common import load_object
import pandas as pd

model = load_object(
    "artifacts/model.pkl"
)

preprocessor = load_object(
    "artifacts/preprocessor.pkl"
)

feature_names = (
    preprocessor.get_feature_names_out()
)

importance = abs(
    model.coef_[0]
)

feature_importance = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

feature_importance = (
    feature_importance
    .sort_values(
        by="Importance",
        ascending=False
    )
)

print(
    feature_importance.head(10)
)