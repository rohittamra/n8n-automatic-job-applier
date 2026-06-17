from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path

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


def save_doc(filename, content):

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / filename

    file_path.write_text(content, encoding="utf-8")

    return str(file_path)
