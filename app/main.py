from fastapi import FastAPI
from .crawler import *

app = FastAPI()


@app.get("/")
async def read_root():
    return read_json()
