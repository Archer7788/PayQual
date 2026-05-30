from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.analyze import router as analyze_router
from app.api.reports import router as reports_router
from app.api.export import router as export_router
from app.api.auth import router as auth_router

from app.database.database import engine
from app.database.database import Base

from app.models.user_model import User
from app.models.report_model import QualityReport

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PayQual API",
    description="AI-powered Data Quality Scoring System",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://pay-qual.vercel.app/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)

app.include_router(analyze_router)

app.include_router(reports_router)

app.include_router(export_router)

app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "PayQual API is running successfully"
    }