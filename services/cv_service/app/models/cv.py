from pydantic import BaseModel, Field
from typing import List, Optional

class JobExperience(BaseModel):
    title: str
    company: str
    duration: str
    details: List[str] = Field(default_factory=list)

class EducationItem(BaseModel):
    degree: str
    institution: str
    duration: str

class CVData(BaseModel):
    name: str
    title: str
    email: str
    phone: str
    address: str
    image_url: Optional[str] = None
    profile: str
    skills: List[str] = Field(default_factory=list)
    languages: List[str] = Field(default_factory=list)
    hobbies: List[str] = Field(default_factory=list)
    education: List[EducationItem] = Field(default_factory=list)
    experience: List[JobExperience] = Field(default_factory=list)
