# app/__init__.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import predict, routes

def create_app():
    app = FastAPI(
        title="VerdictAlign API",
        description="Employee Attrition Prediction & Consistency Analysis",
        version="1.0.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc"
    )
    
    # CORS for frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Update for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    app.include_router(predict.router, prefix="/api/v1", tags=["Predictions"])
    app.include_router(routes.router, tags=["Home"])
    
    return app

# Singleton app instance
app = create_app()