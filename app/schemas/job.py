from pydantic import BaseModel, ConfigDict

class JobBase(BaseModel):
    title: str
    description: str
    company: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
