import joblib
from app.utils.helper import normalize_input

# Load
model = joblib.load("models/xgb_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

# Sample input (same as API)
input_data = {
    "age": 34,
    "department": "Sales",
    "job_role": "Sales Executive",
    "monthly_income": 5000,
    "years_at_company": 3,
    "job_satisfaction": 2,
    "overtime": "Yes",
    "work_life_balance": 2
}

# Normalize
formatted = normalize_input(input_data)

# Transform
X = preprocessor.transform_input(formatted)

# Predict
prediction = model.predict(X)[0]
probability = model.predict_proba(X)[0][1]

print("Prediction:", "Yes" if prediction == 1 else "No")
print("Confidence:", round(probability, 3))