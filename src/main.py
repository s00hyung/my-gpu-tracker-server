from src import crawler
from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    with open("price_list.json", "r") as pl_json:
        pl_dict = json.load(pl_json)
        return pl_dict
