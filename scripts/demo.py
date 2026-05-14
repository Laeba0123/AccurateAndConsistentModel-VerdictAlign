import joblib
from app.utils.helper import normalize_input
from app.core.preprocessing import Preprocessor
from app.core.similarity import SimilarityEngine
from app.core.expectation import ExpectationEngine
from app.core.inconsistency import InconsistencyEngine
from app.core.explainability import ExplainabilityEngine

# =========================
# LOAD COMPONENTS
# =========================
print("\n🚀 Initializing VerdictAlign...\n")

model = joblib.load("models/xgb_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

sim_engine = SimilarityEngine()
exp_engine = ExpectationEngine()
inc_engine = InconsistencyEngine()
explainer = ExplainabilityEngine(model)

print("✅ System Ready!\n")

# =========================
# CLI LOOP
# =========================
while True:

    print("\n==============================")
    print("📥 ENTER EMPLOYEE DETAILS")
    print("==============================")

    try:
        age = int(input("Age: "))
        department = input("Department: ")
        job_role = input("Job Role: ")
        monthly_income = float(input("Monthly Income: "))
        years_at_company = int(input("Years at Company: "))
        job_satisfaction = int(input("Job Satisfaction (1-4): "))
        overtime = input("Overtime (Yes/No): ")
        work_life_balance = int(input("Work Life Balance (1-4): "))

        input_data = {
            "age": age,
            "department": department,
            "job_role": job_role,
            "monthly_income": monthly_income,
            "years_at_company": years_at_company,
            "job_satisfaction": job_satisfaction,
            "overtime": overtime,
            "work_life_balance": work_life_balance
        }

        print("\n📊 Processing...\n")

        # =========================
        # PIPELINE
        # =========================
        formatted = normalize_input(input_data)
        X = preprocessor.transform_input(formatted)

        pred = model.predict(X)[0]
        model_prediction = "Yes" if pred == 1 else "No"

        # Similarity text
        text = f"""
        {formatted['JobRole']} in {formatted['Department']} department,
        age {formatted['Age']}, income {formatted['MonthlyIncome']},
        {formatted['YearsAtCompany']} years experience,
        overtime {formatted['OverTime']},
        satisfaction {formatted['JobSatisfaction']},
        work life balance {formatted['WorkLifeBalance']}
        """

        results = sim_engine.search(text, top_k=50)
        expected = exp_engine.compute(results)
        inconsistency = inc_engine.evaluate(model_prediction, expected)
        explanation = explainer.explain(X, X.columns.tolist())

        # =========================
        # OUTPUT
        # =========================
        print("\n==============================")
        print("📤 RESULT")
        print("==============================")

        print(f"\n🤖 Model Prediction: {model_prediction}")

        print("\n📊 Expected Behavior:")
        print(f"  Majority Vote: {expected['majority_vote']}")
        print(f"  Similar Cases: {expected['similar_cases']}")
        print(f"  Attrition Rate: {expected['attrition_rate']}")

        print("\n⚠️ Inconsistency Check:")
        print(f"  Status: {inconsistency['status']}")
        print(f"  Confidence: {inconsistency['confidence']}")

        print("\n🧠 Top Factors:")
        for feature in explanation["top_features"]:
            print(f"  - {feature}")

        print("\n==============================")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

    # =========================
    # CONTINUE?
    # =========================
    cont = input("\n🔁 Test another case? (y/n): ").lower()
    if cont != 'y':
        print("\n👋 Exiting VerdictAlign. Goodbye!")
        break