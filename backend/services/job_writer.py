from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parents[2]  # repo root

FILE_PATH = BASE_DIR / "files" / "jobs.json"


def save_jobs(jobs):

    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    if FILE_PATH.exists():
        existing = json.loads(FILE_PATH.read_text())
    else:
        existing = []

    existing.extend(jobs)

    FILE_PATH.write_text(json.dumps(existing, indent=2))