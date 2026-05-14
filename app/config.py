import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "xgb_model.pkl")

QDRANT_HOST = "localhost"
QDRANT_PORT = 6333

POSTGRES_URL = "postgresql://user:password@localhost:5432/verdictalign"