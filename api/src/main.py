from fastapi import FastAPI
from enum import Enum
import json

app = FastAPI()


@app.get("/")
async def read_root():
    with open("price_list.json", "r") as pl_json:
        pl_dict = json.load(pl_json)
        return pl_dict


class ModelName(str, Enum):
    rtx3070 = "rtx3070"
    rtx3080 = "rtx3080"
    rtx3090 = "rtx3090"


@app.get("/models/")
async def read_model(name: ModelName):
    return {"model_name": name}
