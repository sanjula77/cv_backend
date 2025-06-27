from fastapi import APIRouter, Request, Form
from fastapi.responses import FileResponse
from app.services.pdf_generator import generate_pdf
from app.models.cv import CVData

router = APIRouter()

@router.post("/generate")
async def generate_cv(data: CVData):
    pdf_path = generate_pdf(data)
    return FileResponse(pdf_path, filename="cv.pdf", media_type="application/pdf")
