from fastapi import FastAPI
from scraper.result_scraper import ResultScraper

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "JNTUH Scraper Running 🔥"}

@app.get("/result/{htno}")
async def get_result(htno: str):
    scraper = ResultScraper(htno)
    result = await scraper.run()

    if not result:
        return {"message": "Result not found"}

    return result
