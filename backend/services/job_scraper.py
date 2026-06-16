import json
from pathlib import Path


def load_jobs():

    file = Path("files/jobs.json")

    if not file.exists():
        return []

    return json.loads(file.read_text())