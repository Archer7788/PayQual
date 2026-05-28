from fastapi import APIRouter

from app.database.database import SessionLocal
from app.models.report_model import QualityReport

router = APIRouter()


@router.get("/reports")
def get_reports():

    db = SessionLocal()

    reports = db.query(QualityReport).all()

    db.close()

    response = []

    for report in reports:

        response.append({
            "id": report.id,
            "filename": report.filename,
            "rows": report.rows,
            "columns": report.columns,
            "completeness_score": report.completeness_score,
            "uniqueness_score": report.uniqueness_score,
            "consistency_score": report.consistency_score,
            "overall_quality_score": report.overall_quality_score
        })

    return response