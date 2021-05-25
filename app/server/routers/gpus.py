from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import database
from ..database import models


router = APIRouter()


@router.get("/gpus", response_description="Return all GPUS")
async def get_gpus():
    gpus = await database.get_all_gpus()
    if gpus:
        return gpus


@router.get("/gpus/{id}", response_description="Return a GPU")
async def get_gpu(id: str):
    gpu = await database.get_a_gpu(id)
    if gpu:
        return gpu


@router.post("/gpu", response_description="Add a new GPU")
async def add_gpu(gpu: models.Gpu = Body(...)):
    gpu_encoded = jsonable_encoder(gpu)
    new_gpu = await database.add_gpu(gpu_encoded)
    return new_gpu
