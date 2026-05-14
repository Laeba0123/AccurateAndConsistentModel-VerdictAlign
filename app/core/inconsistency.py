class InconsistencyEngine:
    def __init__(self):
        pass

    def evaluate(self, model_prediction: str, expected: dict):
        """
        model_prediction: "Yes" or "No"
        expected: output from ExpectationEngine
        """

        majority = expected["majority_vote"]
        attrition_rate = expected["attrition_rate"]

        # Convert to numeric
        pred = 1 if model_prediction == "Yes" else 0
        exp = 1 if majority == "Yes" else 0

        # Check inconsistency
        is_inconsistent = pred != exp

        # Confidence logic
        # Strong disagreement = high confidence
        if is_inconsistent:
            if pred == 1:
                confidence = 1 - attrition_rate
            else:
                confidence = attrition_rate
        else:
            confidence = abs(attrition_rate - 0.5) + 0.5

        return {
            "status": "INCONSISTENT" if is_inconsistent else "CONSISTENT",
            "confidence": round(confidence, 2)
        }