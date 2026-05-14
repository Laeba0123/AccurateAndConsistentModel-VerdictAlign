from fastapi import APIRouter

import app

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/predict")
def predict(data: dict):
    return {
        "prediction": "Yes",
        "consistency": "Consistent"
    }