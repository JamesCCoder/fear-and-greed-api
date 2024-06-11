from fastapi import FastAPI
from app.scraper import get_fear_and_greed_index

app = FastAPI()

@app.get("/fear-and-greed")
def read_fear_and_greed():
    data = get_fear_and_greed_index()
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
