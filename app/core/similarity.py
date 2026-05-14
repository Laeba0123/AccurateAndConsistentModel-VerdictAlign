import os

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


class SimilarityEngine:
    def __init__(self):
        qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
        self.client = QdrantClient(url=qdrant_url)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.collection_name = "hr_attrition"

    # =========================
    # EMBEDDING
    # =========================
    def embed(self, text):
        embedding = self.model.encode([text])
        return embedding[0].tolist()

    # =========================
    # CREATE COLLECTION
    # =========================
    def create_collection(self):
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=384,  # MiniLM embedding size
                distance=Distance.COSINE
            )
        )
        print("✅ Collection created")

    # =========================
    # INSERT DATA
    # =========================
    def insert(self, df):
        points = []

        for idx, row in df.iterrows():

            text = f"""
            {row['JobRole']} in {row['Department']} department,
            age {row['Age']}, income {row['MonthlyIncome']},
            {row['YearsAtCompany']} years experience,
            overtime {row['OverTime']},
            satisfaction {row['JobSatisfaction']},
            work life balance {row['WorkLifeBalance']}
            """

            vector = self.embed(text)

            payload = {
                "Attrition": int(row["Attrition"])
            }

            points.append(
                PointStruct(
                    id=idx,
                    vector=vector,
                    payload=payload
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

        print(f"✅ Inserted {len(points)} records")

    # =========================
    # SEARCH
    # =========================
    def search(self, input_text, top_k=50):
        vector = self.embed(input_text)

        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=top_k
        )

        return results