from pydantic import BaseModel, ConfigDict

class ResumeBase(BaseModel):
    name: str
    email: str
    content: str

class ResumeCreate(ResumeBase):
    pass

class Resume(ResumeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
