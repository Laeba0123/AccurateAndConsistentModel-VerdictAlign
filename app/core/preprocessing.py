import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

class Preprocessor:
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()
        
        self.categorical_cols = ["Department", "JobRole", "OverTime"]
        self.numeric_cols = [
            "Age", "MonthlyIncome", "YearsAtCompany",
            "JobSatisfaction", "WorkLifeBalance"
        ]
        
        self.feature_columns = None
        self.fitted = False

    def load_data(self, path):
        return pd.read_csv(path)

    def select_features(self, df):
        return df[[
            "Age", "Department", "JobRole", "MonthlyIncome",
            "YearsAtCompany", "JobSatisfaction", "OverTime",
            "WorkLifeBalance", "Attrition"
        ]]

    def fit_transform(self, df):
        df = self.select_features(df)
        
        # Create a copy
        X = df.drop("Attrition", axis=1).copy()
        y = df["Attrition"].map({"Yes": 1, "No": 0})
        
        # Encode categorical columns
        for col in self.categorical_cols:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col])
            self.label_encoders[col] = le
        
        # Scale numerical columns
        X[self.numeric_cols] = self.scaler.fit_transform(X[self.numeric_cols])
        
        self.feature_columns = X.columns.tolist()
        self.fitted = True
        
        return X, y

    def transform_input(self, input_data: dict):
        if not self.fitted:
            raise ValueError("❌ Preprocessor not fitted")
        
        df = pd.DataFrame([input_data])
        
        # Encode categorical using saved label encoders
        for col in self.categorical_cols:
            le = self.label_encoders.get(col)
            if le is None:
                raise ValueError(f"❌ Encoder missing for column: {col}")
            
            value = df[col].iloc[0]
            if value in le.classes_:
                df[col] = le.transform([value])[0]
            else:
                print(f"⚠️ Unseen label '{value}' in {col} → using 0")
                df[col] = 0
        
        # Scale numerical
        df[self.numeric_cols] = self.scaler.transform(df[self.numeric_cols])
        
        return df[self.feature_columns]

    def save(self, path):
        joblib.dump(self, path)
        print(f"✅ Preprocessor saved to {path}")

    @staticmethod
    def load(path):
        obj = joblib.load(path)
        if not isinstance(obj, Preprocessor):
            raise ValueError("❌ Loaded object is not Preprocessor")
        print("✅ Preprocessor loaded successfully")
        return obj