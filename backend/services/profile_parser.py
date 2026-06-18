from pathlib import Path
from docx import Document


def parse_resume():

    ROOT = Path(__file__).resolve().parents[2]
    file_path = ROOT / "files" / "resume.docx"

    print("Looking for resume at:", file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Missing resume at {file_path}")

    try:
        doc = Document(str(file_path))
    except Exception as e:
        raise ValueError(
            f"Invalid DOCX file at {file_path}. "
            "File may be corrupted or not a real .docx"
        ) from e

    return "\n".join(
        p.text for p in doc.paragraphs if p.text.strip()
    )