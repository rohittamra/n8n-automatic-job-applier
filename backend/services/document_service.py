from pathlib import Path
from docx import Document

ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = ROOT / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


def write_docx(filename, content):

    path = OUTPUT_DIR / filename

    doc = Document()

    doc.add_paragraph(content)

    doc.save(path)

    return str(path)