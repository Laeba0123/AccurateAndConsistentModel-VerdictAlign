import joblib
from xgboost import XGBClassifier
from app.core.preprocessing import Preprocessor

DATA_PATH = "data/hr_attrition.csv"

# =========================
# LOAD + PREPROCESS
# =========================
preprocessor = Preprocessor()
df = preprocessor.load_data(DATA_PATH)

X, y = preprocessor.fit_transform(df)

# =========================
# TRAIN MODEL
# =========================
model = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    colsample_bytree=0.8,
    eval_metric="logloss"
)

model.fit(X, y)

# =========================
# SAVE
# =========================
joblib.dump(model, "models/xgb_model.pkl")
joblib.dump(preprocessor, "models/preprocessor.pkl")

print("✅ Model and Preprocessor saved successfully!")