from src.utils.common import load_object

model = load_object(
    "artifacts/model.pkl"
)

preprocessor = load_object(
    "artifacts/preprocessor.pkl"
)
# get feature names from preprocessor
feature_names = (
    preprocessor.get_feature_names_out()
)

# extract feature importance
importance = abs(
    model.coef_[0]
)

# create a dataframe for feature importance
import pandas as pd

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