import joblib
from app.utils.helper import normalize_input
from app.core.preprocessing import Preprocessor
from app.core.explainability import ExplainabilityEngine

# Load

model = joblib.load("models/xgb_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

explainer = ExplainabilityEngine(model)

# Input
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

# Explain
result = explainer.explain(X, X.columns.tolist())

print("\n🧠 EXPLANATION:")
print(result)