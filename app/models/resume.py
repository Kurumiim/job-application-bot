from sqlalchemy import Column, Integer, String, Text
from app.models.base import Base

class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    content = Column(Text)
