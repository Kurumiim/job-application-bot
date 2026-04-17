from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine
from app.models import Base
from app.api.v1.router import router

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Job Application Bot API"}

app.include_router(router, prefix="/api/v1")
