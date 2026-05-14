from app.core.similarity import SimilarityEngine

engine = SimilarityEngine()

test_text = """
Sales Executive in Sales department,
age 34, income 5000,
3 years experience,
overtime Yes,
satisfaction 2,
work life balance 2
"""

results = engine.search(test_text, top_k=5)

# FIX: Check if results is a list and print accordingly
print(f"Type of results: {type(results)}")
print(f"Number of results: {len(results) if hasattr(results, '__len__') else 'N/A'}")
print("-" * 50)

# If results is a list of ScoredPoint objects
if isinstance(results, list):
    for idx, r in enumerate(results):
        print(f"Result {idx + 1}:")
        print(f"  Payload: {r.payload}")
        print(f"  Score: {r.score}")
        print("-" * 30)
else:
    # If results is a tuple or other type
    print(f"Results structure: {results}")