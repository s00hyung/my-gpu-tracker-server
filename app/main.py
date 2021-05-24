from fastapi import FastAPI, BackgroundTasks
from .crawler import *

app = FastAPI()

def update_prices():
    start_crawl()

@app.get("/")
def read_root():
    return read_json()

@app.get("/start")
def start_crawling(background_tasks: BackgroundTasks):
    background_tasks.add_task(update_prices)
    return {"status": "Crawler Added To Background Task!"}