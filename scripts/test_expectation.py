from app.core.similarity import SimilarityEngine
from app.core.expectation import ExpectationEngine

engine = SimilarityEngine()
expectation_engine = ExpectationEngine()

test_text = """
Sales Executive in Sales department,
age 34, income 5000,
3 years experience,
overtime Yes,
satisfaction 2,
work life balance 2
"""

results = engine.search(test_text, top_k=20)

expected = expectation_engine.compute(results)

print("\n📊 EXPECTED BEHAVIOR:")
print(expected)