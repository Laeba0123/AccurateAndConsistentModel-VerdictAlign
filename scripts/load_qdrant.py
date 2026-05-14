import pandas as pd
from app.core.similarity import SimilarityEngine

DATA_PATH = "data/hr_attrition.csv"

engine = SimilarityEngine()

df = pd.read_csv(DATA_PATH)

# Keep only required columns
df = df[[
    "Age", "Department", "JobRole", "MonthlyIncome",
    "YearsAtCompany", "JobSatisfaction",
    "OverTime", "WorkLifeBalance", "Attrition"
]]

# Convert target
df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})

# Create collection
engine.create_collection()

# Insert data
engine.insert(df)

print("✅ Data loaded into Qdrant")