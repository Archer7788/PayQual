from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class QualityReport(Base):

    __tablename__ = "quality_reports"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    rows = Column(Integer)

    columns = Column(Integer)

    completeness_score = Column(Float)

    uniqueness_score = Column(Float)

    consistency_score = Column(Float)

    overall_quality_score = Column(Float)