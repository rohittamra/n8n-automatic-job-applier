import json
from pathlib import Path


def save_jobs(jobs: list):

    path = Path("files/jobs.json")
    path.parent.mkdir(exist_ok=True)

    existing = []

    if path.exists():
        try:
            existing = json.loads(path.read_text())
        except:
            existing = []

    # merge + deduplicate by URL
    seen = set(j["url"] for j in existing if "url" in j)

    for job in jobs:
        if job.get("url") not in seen:
            existing.append(job)

    path.write_text(json.dumps(existing, indent=2))