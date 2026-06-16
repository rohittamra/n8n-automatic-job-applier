# backend/services/document_service.py

from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_docx(text, path):

    doc = Document()

    for line in text.split("\n"):
        if line.strip():
            doc.add_paragraph(line)

    doc.save(path)


def create_pdf(text, path):

    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 6))

    doc.build(story)