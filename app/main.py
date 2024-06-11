from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.scraper import get_fear_and_greed_index

app = FastAPI()

# 配置CORS
origins = [
    "http://localhost:3000",
    "http://localhost:3001",  # 允许本地开发的React应用访问
    "https://fear-and-greed-index-290685906189.herokuapp.com"  # 允许您的Heroku应用访问
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/fear-and-greed")
def read_fear_and_greed():
    data = get_fear_and_greed_index()
    if data:
        return data
    else:
        return {"error": "Failed to fetch data"}
