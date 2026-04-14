from fastapi import FastAPI
from app.api.v1.router import router as v1_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
def read_root():
    return {
        "message": "Bem-vindo ao Job Application Bot",
        "project": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "version": settings.APP_VERSION,
    }


app.include_router(v1_router, prefix="/api/v1")
