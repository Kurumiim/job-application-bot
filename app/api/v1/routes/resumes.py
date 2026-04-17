from fastapi import APIRouter, Dependsfrom sqlalchemy import selectfrom sqlalchemy.orm import Sessionfrom app.api.deps import get_dbfrom app.models.resume import Resume as ResumeModelfrom app.schemas.resume import Resume as ResumeSchema, ResumeCreaterouter = APIRouter()@router.post("/", response_model=ResumeSchema)
def create_resume(resume: ResumeCreate, db: Session = Depends(get_db)):
db_resume = ResumeModel(**resume.model_dump())
db.add(db_resume)
db.commit()
db.refresh(db_resume)
return db_resume@router.get("/", response_model=list[ResumeSchema])
def get_resumes(db: Session = Depends(get_db)):
resumes = (
db.execute(select(ResumeModel).order_by(ResumeModel.id.desc()).limit(50))
.scalars()
.all()
)
return resumes
