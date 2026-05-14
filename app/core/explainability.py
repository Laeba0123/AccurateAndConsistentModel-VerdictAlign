import shap
import joblib
import pandas as pd

model = joblib.load("models/xgb_model.pkl")

preprocessor = joblib.load(
    "models/preprocessor.pkl"
)

explainer = shap.TreeExplainer(model)


def generate_explanation(employee_data):

    processed = preprocessor.transform_input(
        employee_data
    )

    shap_values = explainer.shap_values(processed)

    feature_names = processed.columns.tolist()

    contributions = {}

    for i, feature in enumerate(feature_names):

        contributions[feature] = round(
            float(shap_values[0][i]),
            3
        )

    sorted_features = sorted(
        contributions.items(),
        key=lambda x: abs(x[1]),
        reverse=True
    )

    return sorted_features[:5]