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
@router.put("/gpu/{id}", tags=["gpu"])
async def update_gpu(id: str, gpu_data: models.GpuUpdate = Body(...)):
    req = {k: v for k, v in gpu_data.dict().items() if v is not None}
    result = await database.update_gpu(id, req)
    return result


############# CRUD OPERATION (DELETE GPU) #############
@router.delete("/gpu/{id}", tags=["gpu"])
async def delete_gpu(id: str):
    result = await database.delete_gpu(id)
    return result
