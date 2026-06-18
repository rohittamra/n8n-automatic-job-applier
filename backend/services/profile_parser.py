from pathlib import Path
from docx import Document


def parse_resume():

    ROOT = Path(__file__).resolve().parents[2]
    file_path = ROOT / "files" / "resume.docx"

    print("Looking for resume at:", file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Missing resume at {file_path}")

    doc = Document(str(file_path))

    return "\n".join(
        p.text for p in doc.paragraphs if p.text.strip()
    )