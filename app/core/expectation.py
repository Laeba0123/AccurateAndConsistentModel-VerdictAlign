class ExpectationEngine:
    def __init__(self):
        pass

    def compute(self, results):
        """
        results: list of Qdrant points
        """

        total = len(results)
        if total == 0:
            return {
                "majority_vote": "Unknown",
                "similar_cases": 0,
                "attrition_rate": 0.0
            }

        attrition_count = 0

        for r in results:
            if r.payload["Attrition"] == 1:
                attrition_count += 1

        attrition_rate = attrition_count / total

        # Majority voting
        majority = "Yes" if attrition_rate >= 0.5 else "No"

        return {
            "majority_vote": majority,
            "similar_cases": total,
            "attrition_rate": round(attrition_rate, 2)
        }