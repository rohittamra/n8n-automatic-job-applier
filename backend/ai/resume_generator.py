from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_resume(
    linkedin_profile,
    current_resume,
    job_description
):

    prompt = f"""
Create an ATS-friendly resume.

Rules:

- Keep everything truthful
- Add job-relevant keywords
- No tables
- No graphics
- Strong achievement bullets
- ATS optimized

LinkedIn Profile:
{linkedin_profile}

Current Resume:
{current_resume}

Job Description:
{job_description}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text


def structure_resume(text):

    prompt = f"""
Extract structured JSON from this resume:

{text}

Return:
- skills
- roles
- experience
- education
- projects
    """

    return openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    ).choices[0].message.content