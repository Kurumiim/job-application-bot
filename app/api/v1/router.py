from fastapi import APIRouter
from app.api.v1.routes import health, resumes, jobs

router = APIRouter()

router.include_router(health.router, prefix='/health', tags=['health'])
router.include_router(resumes.router, prefix='/resumes', tags=['resumes'])
router.include_router(jobs.router, prefix='/jobs', tags=['jobs'])
