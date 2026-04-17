from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.application import Application
from app.schemas.application import ApplicationCreate, Application

router = APIRouter()

@router.post("/applications/", response_model=Application)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    db_application = Application(**application.dict())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

@router.get("/applications/{application_id}", response_model=Application)
def read_application(application_id: int, db: Session = Depends(get_db)):
    db_application = db.query(Application).filter(Application.id == application_id).first()
    if db_application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    return db_application
