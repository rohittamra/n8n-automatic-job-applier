from openai import OpenAI
import json
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def score_job(job_description: str, profile: str):

    prompt = f"""
        You are an expert recruiter.

        Candidate Profile:
        {profile}

        Job Description:
        {job_description}

        Return JSON:

        {{
        "score": 0-100,
        "reasons": [],
        "missing_skills": []
        }}
        """

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return json.loads(response.output_text)