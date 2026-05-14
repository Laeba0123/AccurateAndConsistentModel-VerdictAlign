from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Correct imports
from ..core.modle_handler import predict_attrition
from ..core.inconsistency import InconsistencyEngine
from ..core.expectation import ExpectationEngine
from ..core.explainability import generate_explanation

router = APIRouter()

# Initialize engines
expectation_engine = ExpectationEngine()
inconsistency_engine = InconsistencyEngine()


# Input schema
class EmployeeInput(BaseModel):
    Age: int
    Department: str
    JobRole: str
    MonthlyIncome: int
    YearsAtCompany: int
    JobSatisfaction: int
    OverTime: str
    WorkLifeBalance: int


@router.post("/predict")
def predict(employee: EmployeeInput):

    try:

        # Convert request to dictionary
        employee_data = employee.dict()

        # ML prediction
        prediction_label, probability = predict_attrition(employee_data)

        # Mock similar historical cases
        class MockPoint:
            def __init__(self, attrition):
                self.payload = {"Attrition": attrition}

        mock_search_results = [
            MockPoint(1),
            MockPoint(1),
            MockPoint(0)
        ]

        # Expected historical behavior
        expectation = expectation_engine.compute(
            mock_search_results
        )

        # Consistency evaluation
        inconsistency = inconsistency_engine.evaluate(
            model_prediction=prediction_label,
            expected=expectation
        )

        # SHAP explanation
        explanation = generate_explanation(
            employee_data
        )

        # Final response
        return {
            "prediction": prediction_label,
            "probability": round(float(probability), 2),
            "expected_behavior": expectation,
            "consistency_status": inconsistency,
            "explanation": explanation
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )