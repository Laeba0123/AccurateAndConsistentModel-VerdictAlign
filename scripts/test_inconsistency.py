import joblib
from app.utils.helper import normalize_input
from app.core.preprocessing import Preprocessor
from app.core.similarity import SimilarityEngine
from app.core.expectation import ExpectationEngine
from app.core.inconsistency import InconsistencyEngine

# Load components
model = joblib.load("models/xgb_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

sim_engine = SimilarityEngine()
exp_engine = ExpectationEngine()
inc_engine = InconsistencyEngine()

# Input (same as API)
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

# ML Prediction
X = preprocessor.transform_input(formatted)
pred = model.predict(X)[0]
model_prediction = "Yes" if pred == 1 else "No"

# Build text for similarity
text = f"""
{formatted['JobRole']} in {formatted['Department']} department,
age {formatted['Age']}, income {formatted['MonthlyIncome']},
{formatted['YearsAtCompany']} years experience,
overtime {formatted['OverTime']},
satisfaction {formatted['JobSatisfaction']},
work life balance {formatted['WorkLifeBalance']}
"""

# Similarity
results = sim_engine.search(text, top_k=50)

# Expectation
expected = exp_engine.compute(results)

# Inconsistency
decision = inc_engine.evaluate(model_prediction, expected)

# Output
print("\n🔍 FINAL ANALYSIS\n")
print("Model Prediction:", model_prediction)
print("Expected Behavior:", expected)
print("Inconsistency Check:", decision)