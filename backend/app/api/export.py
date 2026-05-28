from fastapi import APIRouter

from fastapi.responses import FileResponse

from app.database.database import SessionLocal

from app.models.report_model import (
    QualityReport
)

from app.utils.pdf_generator import (
    generate_pdf_report
)

router = APIRouter()


@router.get("/export/{report_id}")
def export_report(report_id: int):

    db = SessionLocal()

    report = (
        db.query(QualityReport)
        .filter(
            QualityReport.id == report_id
        )
        .first()
    )

    db.close()

    if not report:

        return {
            "error": "Report not found"
        }

    filepath = f"report_{report_id}.pdf"

    generate_pdf_report(
        filepath,
        report
    )

    return FileResponse(
        path=filepath,
        filename=filepath,
        media_type="application/pdf"
    )