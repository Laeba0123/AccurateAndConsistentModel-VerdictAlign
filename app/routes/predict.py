from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Ensure these match your actual file structure
from ..core.modle_handler import predict_attrition as ModelHandler 
from ..core.inconsistency import InconsistencyEngine
from ..core.expectation import ExpectationEngine
from ..core.explainability import generate_explanation 

router = APIRouter()

# Instantiate handlers once to maintain state/efficiency
model_handler = ()
expectation_engine = ExpectationEngine()
inconsistency_engine = InconsistencyEngine()


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
        employee_data = employee.dict()

        prediction_label, probability = ModelHandler(employee_data)
        prediction_idx = 1 if prediction_label == "Yes" else 0

        class MockPoint:
            def __init__(self, attrition):
                self.payload = {"Attrition": attrition}
        
        # Example: Mocking historical similar cases
        mock_search_results = [MockPoint(1), MockPoint(1), MockPoint(0)]
        expectation = expectation_engine.compute(mock_search_results) 

        # 3. Consistency check
        inconsistency = inconsistency_engine.evaluate(
            model_prediction=prediction_label,
            expected=expectation
        )

        # 4. Explanation logic
        explanation= generate_explanation(employee_data)

        return {
            "prediction": prediction_label,
            "probability": round(probability, 2),
            "expected_behavior": expectation,
            "consistency_status": inconsistency,
            "explanation": explanation
        }
    except Exception as e:
        # This catches the error seen in image_494a33.png and explains it
        raise HTTPException(status_code=500, detail=str(e))