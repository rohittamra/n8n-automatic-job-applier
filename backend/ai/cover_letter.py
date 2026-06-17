from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_cover_letter(job, profile):

    prompt = f"""
        You are an expert technical recruiter.

        Generate a highly personalized cover letter.

        JOB:
        {job['description']}

        COMPANY:
        {job['company']}

        CANDIDATE PROFILE:
        {profile}

        Make it:
        - ATS optimized
        - specific to job
        - senior DevOps/Cloud tone
        """

    return openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    ).choices[0].message.content