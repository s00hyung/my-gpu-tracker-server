from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import database
from ..database import models


router = APIRouter()


@router.get("/gpus", tags=["gpus"])
async def get_gpus():
    result = await database.get_all_gpus()
    return result


############# CRUD OPERATION (CREATE GPU) #############
@router.post("/gpu", tags=["gpu"])
async def add_gpu(gpu_data: models.Gpu = Body(...)):
    gpu_encoded = jsonable_encoder(gpu_data)
    result = await database.add_gpu(gpu_encoded)
    return result


############# CRUD OPERATION (READ GPU) #############
@router.get("/gpu/{id}", tags=["gpu"])
async def get_gpu(id: str, response_model_exclude_unset=True):
    result = await database.get_gpu(id)
    return result


############# CRUD OPERATION (UPDATE GPU) #############
@router.put("/gpu", tags=["gpu"])
async def update_gpu(id: str, gpu_data: models.GpuUpdate = Body(...)):
    encoded = jsonable_encoder(gpu_data)
    print(encoded)
    result = await database.update_gpu(id, encoded)
    return result


############# CRUD OPERATION (DELETE GPU) #############
@router.delete("/gpu", tags=["gpu"])
async def delete_gpu(id: str):
    result = await database.delete_gpu(id)
    return result


############# CRUD OPERATION (CREATE PRICE) #############
@router.post("/gpu/price", tags=["price"])
async def add_gpu_price(id: str, price: models.Price = Body(...)):
    price_encoded = jsonable_encoder(price)
    result = await database.add_gpu_price(id, price_encoded)
    return result


############# CRUD OPERATION (READ PRICE) #############
@router.get("/gpu/price/{id}", tags=["price"])
async def get_gpu_price(id: str, response_model_exclude_unset=True):
    result = await database.get_gpu_price(id)
    return result


############# CRUD OPERATION (UPDATE PRICE) #############
@router.put("/gpu/price/{id}", tags=["price"])
async def update_gpu_price(id: str, price_data: models.PriceUpdate = Body(...)):
    price_encoded = jsonable_encoder(price_data)
    result = await database.update_gpu_price(id, price_encoded)
    return result


############# CRUD OPERATION (DELETE PRICE) #############
@router.delete("/gpu/price/{id}", tags=["price"])
async def delete_gpu_price(id: str, date: str):
    result = await database.delete_gpu_price(id, date)
    return result
