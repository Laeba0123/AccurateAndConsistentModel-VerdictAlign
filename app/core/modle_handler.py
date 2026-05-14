import joblib
import pandas as pd

model = joblib.load("models/xgb_model.pkl")

preprocessor = joblib.load(
    "models/preprocessor.pkl"
)


def predict_attrition(employee_data):

    df = pd.DataFrame([employee_data])

    processed = preprocessor.transform_input(
        employee_data
    )

    prediction = model.predict(processed)[0]

    probability = model.predict_proba(
        processed
    )[0][1]

    label = "Yes" if prediction == 1 else "No"

    return label, round(float(probability), 2)