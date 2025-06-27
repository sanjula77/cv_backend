import pdfkit
from jinja2 import Environment, FileSystemLoader
from app.models.cv import CVData
import os

def generate_pdf(data: CVData):
    env = Environment(loader=FileSystemLoader("app/templates"))
    template = env.get_template("cv_template.html")
    html_content = template.render(cv=data)

    output_path = f"app/static/{data.name.replace(' ', '_')}_cv.pdf"
    pdfkit.from_string(html_content, output_path)

    return output_path
