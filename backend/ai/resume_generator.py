from openai import OpenAI
from services.document_service import write_docx

client = OpenAI()


def generate_resume(job, profile):

    prompt = f"""
Tailor this resume for the job.

JOB:
{job}

PROFILE:
{profile}

Return only resume text.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    text = response.output_text

    filename = (
        f"resume_"
        f"{job['company']}.docx"
        .replace(" ", "_")
    )

    return write_docx(
        filename,
        text
    )