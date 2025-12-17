import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL = "http://results.jntuh.ac.in/resultAction"

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "exam_codes.json"


class ResultScraper:
    def __init__(self, hallticket: str):
        self.hallticket = hallticket.upper()

        with open(DATA_PATH, "r", encoding="utf-8") as f:
            self.exam_codes = json.load(f)["btech"]

    async def fetch(self, session, exam_code):
        params = (
            f"?examCode={exam_code}"
            f"&degree=btech"
            f"&etype=r17"
            f"&result=null"
            f"&grad=null"
            f"&type=intgrade"
            f"&htno={self.hallticket}"
        )

        async with session.get(BASE_URL + params, timeout=15) as res:
            return await res.text()

    def parse_html(self, html):
        soup = BeautifulSoup(html, "lxml")
        tables = soup.find_all("table")

        if len(tables) < 2:
            return None

        details_table = tables[0]
        marks_table = tables[1]

        rows = details_table.find_all("tr")
        if len(rows) < 2:
            return None

        htno = rows[0].find_all("td")[1].text.strip()
        name = rows[0].find_all("td")[3].text.strip()
        college = rows[1].find_all("td")[3].text.strip()

        subjects = []
        for row in marks_table.find_all("tr")[1:]:
            cols = row.find_all("td")
            if len(cols) >= 3:
                subjects.append({
                    "subjectCode": cols[0].text.strip(),
                    "subjectName": cols[1].text.strip(),
                    "grade": cols[-1].text.strip()
                })

        return {
            "details": {
                "rollNo": htno,
                "name": name,
                "college": college
            },
            "subjects": subjects
        }

    async def run(self):
        async with aiohttp.ClientSession() as session:
            for code in self.exam_codes:
                try:
                    html = await self.fetch(session, code)
                    result = self.parse_html(html)
                    if result:
                        return result
                except Exception:
                    continue

        return None
