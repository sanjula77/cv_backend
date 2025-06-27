from pydantic import BaseModel
from typing import List, Optional

class JobExperience(BaseModel):
    title: str
    company: str
    duration: str
    details: List[str]

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
    image_url: Optional[str] = None  # Add image support
    profile: str
    skills: List[str]
    languages: List[str]
    hobbies: List[str]
    education: List[EducationItem]
    experience: List[JobExperience]
