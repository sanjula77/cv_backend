from pydantic import BaseModel
from typing import List

class CVData(BaseModel):
    name: str
    title: str
    email: str
    phone: str
    address: str
    education: List[str]
    experience: List[str]
    skills: List[str]
    languages: List[str]
