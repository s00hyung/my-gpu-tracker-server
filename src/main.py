from src import crawler
from fastapi import FastAPI
import crawler

app = FastAPI()


@app.get("/")
async def read_root():
    return crawler.read_json()
