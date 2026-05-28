from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import letter


def generate_pdf_report(
    filepath,
    report
):

    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "PayQual Data Quality Report",
        styles["Title"]
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    fields = [

        ("Filename", report.filename),

        ("Rows", report.rows),

        ("Columns", report.columns),

        (
            "Completeness Score",
            report.completeness_score
        ),

        (
            "Uniqueness Score",
            report.uniqueness_score
        ),

        (
            "Consistency Score",
            report.consistency_score
        ),

        (
            "Overall Quality Score",
            report.overall_quality_score
        )
    ]

    for label, value in fields:

        paragraph = Paragraph(
            f"<b>{label}:</b> {value}",
            styles["BodyText"]
        )

        elements.append(paragraph)

        elements.append(
            Spacer(1, 12)
        )

    doc.build(elements)