import pdfkit
from jinja2 import Environment, FileSystemLoader
from app.models.cv import CVData
import os

def generate_pdf(data: CVData):
    env = Environment(loader=FileSystemLoader("app/templates"))
    template = env.get_template("cv_template.html")
    html_content = template.render(cv=data)

    output_path = f"app/static/{data.name.replace(' ', '_')}_cv.pdf"

    # Manually set path to wkhtmltopdf.exe
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    # Generate the PDF
    pdfkit.from_string(html_content, output_path, configuration=config)

    return output_path
