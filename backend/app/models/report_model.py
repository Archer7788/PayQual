from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base
from sqlalchemy import ForeignKey

class QualityReport(Base):

    __tablename__ = "quality_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
    Integer,
    ForeignKey("users.id")
)
    filename = Column(String)

    rows = Column(Integer)

    columns = Column(Integer)

    completeness_score = Column(Float)

    uniqueness_score = Column(Float)

    consistency_score = Column(Float)

    overall_quality_score = Column(Float)