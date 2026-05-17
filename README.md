# ⚖️ VerdictAlign
Hybrid AI Decision Engine for Employee Attrition Prediction with Explainable Consistency Checking
Predict employee attrition with explainable machine learning, semantic similarity retrieval, and consistency-aware validation designed for reliable HR decision intelligence.

<p align="left"> <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" /> <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react" /> <img src="https://img.shields.io/badge/XGBoost-FF6F00?style=for-the-badge" /> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel" /> <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render" /> <img src="https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge" /> <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" /> </p>

# Table of Contents
Overview
Live Demo & API Access
Key Features
System Architecture
Technology Stack
Machine Learning Pipeline
Explainability & Validation Layer
API Documentation
Frontend Overview
Deployment Architecture
Local Development Setup
Project Structure
Screenshots / Demo
Future Improvements
Contributing
License
Author
Overview

VerdictAlign is a hybrid AI-powered employee attrition prediction and validation platform designed to improve reliability and transparency in HR analytics systems.

Traditional predictive models typically generate decisions based solely on statistical probability. VerdictAlign extends this paradigm by integrating:

Predictive machine learning
Semantic similarity retrieval
Explainable AI
Historical expectation analysis
Decision consistency validation

The system evaluates whether a generated prediction aligns with historically similar employee behaviors before presenting the final result.

This architecture enables more trustworthy and interpretable AI-assisted workforce analytics suitable for enterprise HR environments, academic research, and intelligent decision support systems.

# Live Demo & API Access

## Frontend Application
🚀 https://accurate-and-consistent-model-verdi-ruby.vercel.app

## Backend Swagger Documentation

📄 https://accurateandconsistentmodel-verdictalign-9.onrender.com/docs

## Backend API Base URL
https://accurateandconsistentmodel-verdictalign-9.onrender.com

## Key Features
## 🤖 Machine Learning Prediction

Uses an optimized XGBoost classifier trained on HR attrition data to predict employee resignation risk.

## 🧠 Explainable AI (SHAP)

Provides feature-level interpretability by identifying the major drivers influencing prediction outcomes.

## 🔍 Semantic Similarity Retrieval
Retrieves historically similar employee profiles using Sentence-Transformers embeddings and vector similarity search.

## ⚖️ Consistency Validation Engine
Compares model predictions against behavioral patterns from retrieved historical cases to detect inconsistencies.

## 📊 Interactive Analytics Dashboard
Modern React-based frontend with responsive charts, motion effects, and API-driven visualization.

# 🚀 Production Deployment
Full-stack deployment using Vercel (frontend) and Render (backend) with scalable API architecture.

## System Architecture

                           ┌───────────────────────┐
                           │        User           │
                           └──────────┬────────────┘
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │   React Frontend (Vercel)      │
                    │  Dashboard • Charts • Forms    │
                    └──────────┬─────────────────────┘
                               │ REST API Calls
                               ▼
                 ┌───────────────────────────────────┐
                 │      FastAPI Backend (Render)     │
                 │ Authentication • Validation • API │
                 └──────────┬────────────────────────┘
                            │
        ┌───────────────────┼────────────────────┐
        ▼                   ▼                    ▼
    ┌──────────────┐   ┌────────────────┐   ┌─────────────────┐
    │ XGBoost ML   │   │ SHAP Engine    │   │ Retrieval Layer │
    │ Prediction   │   │ Explainability │   │ Semantic Search │
    └──────┬───────┘   └──────┬─────────┘   └────────┬────────┘
           │                  │                      │
           ▼                  ▼                      ▼
    ┌────────────┐   ┌──────────────┐      ┌────────────────┐
    │ Prediction │   │ Feature      │      │ Qdrant Vector  │
    │ Probability│   │ Contributions│      │ Database       │
    └─────┬──────┘   └──────┬───────┘      └────────┬───────┘
          └─────────────────┼───────────────────────┘
                            ▼
             ┌──────────────────────────┐
             │ Validation & Consistency │
             │ Expectation Analysis     │
             │ Inconsistency Detection  │
             └──────────┬───────────────┘
                        ▼
             ┌──────────────────────────┐
             │ Final Decision Response  │
             │ + Explainability Report  │
             └──────────────────────────┘
             
##  Technology Stack
- Category	Technologies
- Frontend	React 18, Vite, Tailwind CSS, Framer Motion, Axios, Recharts
- Backend	FastAPI, Uvicorn, Gunicorn, Pydantic
- Machine Learning	XGBoost, Scikit-learn, Pandas, NumPy
- Explainability	SHAP
- NLP & Similarity	Sentence-Transformers
- Vector Database	Qdrant
- Deployment	Vercel, Render
- Version Control	Git, GitHub
- Machine Learning Pipeline

## 1. Data Preprocessing

The HR dataset undergoes preprocessing and feature engineering before model training:

- Missing value handling
- Categorical encoding
- Feature normalization
- Structured HR feature selection
- Selected Features
- Feature	Description
- Age	Employee age
- Department	Organizational department
- JobRole	Employee role
- MonthlyIncome	Monthly salary
- YearsAtCompany	Organizational tenure
- JobSatisfaction	Satisfaction rating
- OverTime	Overtime status
- WorkLifeBalance	Work-life balance score

## 2. Feature Engineering

Structured employee records are transformed into machine-readable representations suitable for both:

Predictive modeling
Semantic similarity retrieval

Textual representations are generated for embedding-based retrieval.

## 3. Model Training

The system uses XGBoost for binary attrition classification due to:

- Strong predictive performance
- Gradient boosting optimization
- Robust handling of structured tabular data
- Regularization support

## 4. Semantic Similarity Search

Employee records are embedded using Sentence-BERT embeddings and stored inside Qdrant vector collections.

Nearest-neighbor retrieval enables contextual comparison against historically similar employee cases.

## 5. Explainability Layer

SHAP explanations identify influential features contributing to each prediction outcome.

Example influential features include:

- Overtime
- Monthly income
- Job satisfaction
- Work-life balance
- Years at company

## 6. Consistency Validation

The consistency engine compares:

Current model prediction
Majority historical behavior from retrieved cases

This additional validation layer improves reliability and decision transparency.

Explainability & Validation Layer
SHAP-Based Explainability

VerdictAlign integrates SHAP (SHapley Additive Explanations) to improve interpretability of model outputs.

The system identifies:

- Which features influenced prediction decisions
- Relative contribution of each feature
- Positive and negative prediction drivers
- Similarity Retrieval Engine

Semantic embeddings generated using Sentence-Transformers are indexed in Qdrant for high-speed similarity search.

This enables:

- Context-aware retrieval
- Historical pattern comparison
- Behavioral expectation estimation
- Expectation Analysis

Retrieved employee cases are analyzed to estimate expected historical behavior patterns.

The engine evaluates:

- Attrition frequency
- Majority behavioral trends
- Similar case distribution
- Inconsistency Detection

If the machine learning prediction conflicts with historically similar cases, the system flags the result as potentially inconsistent.

This creates an additional reliability layer beyond raw prediction probability.

- API Documentation
- Main Endpoint
- Method	Endpoint	Description
- POST	/api/v1/predict	Predict employee attrition and perform consistency validation
Example Request
```
{
  "age": 34,
  "department": "Sales",
  "job_role": "Sales Executive",
  "monthly_income": 5000,
  "years_at_company": 3,
  "job_satisfaction": 2,
  "overtime": "Yes",
  "work_life_balance": 2
}
```
Example Response
```
{
  "prediction": "Yes",
  "confidence": 0.87,
  "expected_behavior": {
    "majority_vote": "Yes",
    "similar_cases": 50,
    "attrition_rate": 0.74
  },
  "consistency_check": {
    "status": "Consistent",
    "confidence": 0.81
  },
  "top_features": [
    "OverTime",
    "MonthlyIncome",
    "WorkLifeBalance"
  ]
}
```
cURL Example
```
curl -X POST \
"https://accurateandconsistentmodel-verdictalign-9.onrender.com/api/v1/predict" \
-H "Content-Type: application/json" \
-d '{
  "age": 34,
  "department": "Sales",
  "job_role": "Sales Executive",
  "monthly_income": 5000,
  "years_at_company": 3,
  "job_satisfaction": 2,
  "overtime": "Yes",
  "work_life_balance": 2
}'
```
Swagger Documentation
https://accurateandconsistentmodel-verdictalign-9.onrender.com/docs

Frontend Overview
The frontend is built using React 18 and Vite for high-performance rendering and modular UI development.

- Frontend Capabilities
- Responsive dashboard UI
- API-driven analytics visualization
- Interactive charts using Recharts
- Smooth animations with Framer Motion
- Real-time prediction interaction
- Modern Tailwind-based styling
- Deployment Architecture
- Frontend Deployment — Vercel

The frontend application is deployed using Vercel for:

- Edge delivery
- Fast static asset serving
- Automatic GitHub deployment integration
- Backend Deployment — Render

The FastAPI backend is deployed on Render using:

- Gunicorn
- Uvicorn workers
- Production API routing
- Deployment Workflow
```
GitHub Push
     │
     ├──────────────► Vercel Frontend Deployment
     │
     └──────────────► Render Backend Deployment
```
Render Blueprint
services:
    type: web
    name: verdictalign-api
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app.main:app -k uvicorn.workers.UvicornWorker
Local Development Setup
Clone Repository
```
git clone https://github.com/your-username/verdictalign.git
cd verdictalign
Backend Setup
Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run Backend
uvicorn app.main:app --reload
```

Backend runs at:
```
http://127.0.0.1:8000
Frontend Setup
cd frontend
npm install
npm run dev
```

Frontend runs at:
```
http://localhost:5173
```
Environment Variables
```
Create a .env file:

API_BASE_URL=http://127.0.0.1:8000
Project Structure
VerdictAlign/
│
├── app/                         # FastAPI backend
│   ├── api/                     # API routes
│   ├── core/                    # ML engines & logic
│   ├── utils/                   # Helper utilities
│   └── main.py                  # FastAPI entrypoint
│
├── frontend/                    # React frontend
│   ├── src/
│   ├── public/
│   └── vite.config.js
│
├── models/                      # Serialized ML models
│   ├── xgb_model.pkl
│   └── preprocessor.pkl
│
├── data/                        # Dataset storage
│
├── render.yaml                  # Render deployment config
├── vercel.json                  # Vercel deployment config
├── docker-compose.yml           # Container orchestration
├── requirements.txt             # Python dependencies
└── README.md
```
Screenshots / Demo
Dashboard Preview

Add frontend dashboard screenshot here

Prediction Result Interface

Add prediction output screenshot here

Swagger API Documentation

Add Swagger /docs screenshot here

- Future Improvements
- Dockerized microservice deployment
- Authentication & RBAC
- Real-time HR analytics dashboards
- CI/CD automation pipelines
- Advanced model monitoring
- Multi-model ensemble validation
- Kubernetes deployment support
- Streaming inference architecture
- PDF report export functionality
- LLM-assisted HR recommendation engine
- Contributing

Contributions are welcome.

To contribute:

- Fork the repository
- Create a feature branch
- Commit changes
- Push updates
- Open a pull request
## License

This project is licensed under the MIT License.

## Author

Laeba Jamil

GitHub: https://github.com/your-username
LinkedIn: https://linkedin.com/in/your-profile
<p align="center"> Built with reliability, explainability, and production-grade AI engineering principles. </p>
