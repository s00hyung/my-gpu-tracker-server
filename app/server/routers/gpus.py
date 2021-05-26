from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import database
from ..database import models


router = APIRouter()


@router.get("/gpus")
async def get_gpus():
    gpus = await database.get_all_gpus()
    if gpus:
        return gpus


############# CRUD OPERATION (CREATE) #############
@router.post("/gpu")
async def add_gpu(gpu: models.Gpu = Body(...)):
    gpu_encoded = jsonable_encoder(gpu)
    new_gpu = await database.add_gpu(gpu_encoded)
    return new_gpu


############# CRUD OPERATION (READ) #############
@router.get("/gpus/{id}")
async def get_gpu(id: str, response_model_exclude_unset=True):
    gpu = await database.get_gpu(id)
    if gpu:
        return gpu


############# CRUD OPERATION (UPDATE) #############
@router.put("/gpu")
async def update_gpu():
    pass


############# CRUD OPERATION (DELETE) #############
@router.delete("/gpu")
async def delete_gpu(id: str):
    result = await database.delete_gpu(id)
    return result


@router.post("/gpu/price")
async def add_gpu_price(id: str, price: models.Price):
    price_encoded = jsonable_encoder(price)
    new_price = await database.add_price_of_gpu(id, price_encoded)
    return new_price
