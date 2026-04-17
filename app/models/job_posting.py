from sqlalchemy import Column, Integer, String, Text
from app.models.base import Base

class JobPosting(Base):
    __tablename__ = "job_postings"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    company = Column(String)
