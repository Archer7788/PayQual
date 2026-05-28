from fastapi import APIRouter, UploadFile, File
import pandas as pd
import os

from app.ai_engine.quality_analyzer import generate_quality_report

from app.database.database import SessionLocal
from app.models.report_model import QualityReport
from app.ai_engine.llm_analyzer import (
    generate_ai_summary
)
from app.validators.data_validator import (
    validate_email_columns,
    validate_phone_columns,
    detect_duplicate_rows,
    detect_outliers
)

router = APIRouter()

UPLOAD_FOLDER = "app/uploads"


@router.post("/analyze")
async def analyze_dataset(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    # Read dataset
    if file.filename.endswith(".csv"):

        df = pd.read_csv(file_path)

    elif file.filename.endswith(".xlsx"):

        df = pd.read_excel(file_path)

    else:
        return {
            "error": "Unsupported file format"
        }

    report = generate_quality_report(df)
    invalid_emails = (
    validate_email_columns(df)
    )

    invalid_phones = (
    validate_phone_columns(df)
    )

    duplicate_rows = (
    detect_duplicate_rows(df)
    )

    outlier_count = (
    detect_outliers(df)
    )  
    ai_summary = generate_ai_summary(
    report
    )
    

    # DATABASE SESSION
    db = SessionLocal()

    db_report = QualityReport(
        filename=file.filename,
        rows=int(df.shape[0]),
        columns=int(df.shape[1]),
        completeness_score=float(report["completeness_score"]),
        uniqueness_score=float(report["uniqueness_score"]),
        consistency_score=float(report["consistency_score"]),
        overall_quality_score=float(report["overall_quality_score"])
    )

    db.add(db_report)

    db.commit()

    db.refresh(db_report)

    db.close()

    return {
        "filename": file.filename,
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "quality_report": report,
        "ai_summary": ai_summary,
        "validation_results": {

        "invalid_emails":
            invalid_emails,

        "invalid_phones":
            invalid_phones,

        "duplicate_rows":
            duplicate_rows,

        "outlier_count":
            outlier_count
        }
    }