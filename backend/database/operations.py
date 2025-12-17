import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

async def get_exam_codes(degree, regulation):
    path = BASE_DIR / "data" / "exam_codes.json"
    with open(path, "r") as f:
        data = json.load(f)

    return data.get(degree, {}).get(regulation, {})
