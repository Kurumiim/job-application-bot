from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.job_posting import JobPosting
from app.schemas.job import Job, JobCreate

router = APIRouter()

@router.post("/", response_model=Job)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = JobPosting(**job.model_dump())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/", response_model=list[Job])
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.execute(select(JobPosting).order_by(JobPosting.id.desc()).limit(50)).scalars().all()
    return jobs
