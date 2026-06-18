from docx import Document
from pathlib import Path


def parse_resume(path="files/resume.docx"):

    BASE_DIR = Path(__file__).resolve().parents[2]  # repo root
    file_path = BASE_DIR / path

    if not file_path.exists():
        raise FileNotFoundError(f"Resume not found at {file_path}")

    doc = Document(str(file_path))

    return "\n".join(
        p.text for p in doc.paragraphs if p.text.strip()
    )