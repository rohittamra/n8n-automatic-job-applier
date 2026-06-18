from openai import OpenAI
from services.document_service import write_docx

client = OpenAI()


def generate_cover_letter(job, profile):

    prompt = f"""
Write a tailored cover letter.

JOB:
{job}

PROFILE:
{profile}

Return only the cover letter.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    text = response.output_text

    filename = (
        f"cover_letter_"
        f"{job['company']}.docx"
        .replace(" ", "_")
    )

    return write_docx(
        filename,
        text
    )