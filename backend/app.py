from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Body
from services.job_writer import save_jobs

from ai.scorer import score_job
from ai.resume_generator import generate_resume
from ai.cover_letter import generate_cover_letter

app = FastAPI(
    title="AI Job Automation"
)


class JobRequest(BaseModel):
    job_description: str
    profile: str


@app.post("/score")
def score(request: JobRequest):

    return score_job(
        request.job_description,
        request.profile
    )


class ResumeRequest(BaseModel):

    linkedin_profile: str

    current_resume: str

    job_description: str


@app.post("/generate-resume")
def resume(request: ResumeRequest):

    return {
        "resume": generate_resume(
            request.linkedin_profile,
            request.current_resume,
            request.job_description
        )
    }


class CoverLetterRequest(BaseModel):

    company: str

    role: str

    resume_text: str

    job_description: str


@app.post("/generate-cover-letter")
def cover_letter(request: CoverLetterRequest):

    return {
        "cover_letter": generate_cover_letter(
            request.company,
            request.role,
            request.resume_text,
            request.job_description
        )
    }

@app.post("/jobs/update")
def update_jobs(jobs: list = Body()):
    save_jobs(jobs)
    return {"status": "saved", "count": len(jobs)}

@app.get("/")
def root():
    return {
        "status": "running"
    }