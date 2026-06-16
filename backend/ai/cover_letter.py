from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_cover_letter(
    company,
    role,
    resume_text,
    job_description
):

    prompt = f"""
Create a professional cover letter.

Company:
{company}

Role:
{role}

Resume:
{resume_text}

Job Description:
{job_description}

Keep it under 350 words.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text