import json
import os
from pathlib import Path

from services.profile_parser import parse_resume
from ai.scorer import score_job
from ai.resume_generator import generate_resume
from ai.cover_letter import generate_cover_letter

ROOT = Path(__file__).resolve().parents[1]

FILES_DIR = ROOT / "files"
OUTPUT_DIR = ROOT / "output"

JOBS_FILE = FILES_DIR / "jobs.json"


def load_jobs():
    if not JOBS_FILE.exists():
        return []

    with open(JOBS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_results(results):
    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(
        OUTPUT_DIR / "results.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(results, f, indent=2)


def main():

    profile = parse_resume()

    jobs = load_jobs()

    threshold = int(
        os.getenv(
            "JOB_SCORE_THRESHOLD",
            "75"
        )
    )

    results = []

    for job in jobs:

        score_data = score_job(
            job["description"],
            profile
        )

        score = score_data.get("score", 0)

        if score < threshold:
            continue

        tailored_resume = generate_resume(
            job,
            profile
        )

        tailored_cover = generate_cover_letter(
            job,
            profile
        )

        results.append(
            {
                "title": job["title"],
                "company": job["company"],
                "score": score,
                "reasons": score_data.get(
                    "reasons",
                    []
                ),
                "missing_skills": score_data.get(
                    "missing_skills",
                    []
                ),
                "resume_file": tailored_resume,
                "cover_letter_file": tailored_cover,
            }
        )

    save_results(results)

    print(
        f"Processed {len(jobs)} jobs. "
        f"Matched {len(results)} jobs."
    )


if __name__ == "__main__":
    main()