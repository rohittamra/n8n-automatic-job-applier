from docx import Document


def parse_resume(path="files/resume.docx"):

    doc = Document(path)

    text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

    return text