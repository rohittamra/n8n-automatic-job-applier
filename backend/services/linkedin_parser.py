from pathlib import Path


def load_linkedin_profile():

    path = Path("files/linkedin_profile.txt")

    if not path.exists():
        return ""

    return path.read_text(encoding="utf-8")