import motor.motor_asyncio
from dotenv import dotenv_values

config = dotenv_values(".env")
un = config["MONGO_DB_USERNAME"]
pw = config["MONGO_DB_PASSWORD"]
url = config["MONGO_DB_URL"]

MONGODB_URL = f"mongodb+srv://{un}:{pw}@{url}"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client.gpu_database
gpu_collection = database.get_collection("gpu_collection")


async def get_all_gpus():
    gpus = []
    async for gpu in gpu_collection.find():
        gpus.append(gpu)
    return gpus


############# CRUD OPERATION (CREATE) #############
async def add_gpu(gpu_data: dict):
    gpu = await gpu_collection.insert_one(gpu_data)
    new_gpu = await gpu_collection.find_one({"_id": gpu.inserted_id}, {"_id": 0})
    return new_gpu


############# CRUD OPERATION (READ) #############
async def get_gpu(id: str):
    gpu = await gpu_collection.find_one({"_id": id})
    if gpu:
        return gpu
    else:
        return None


############# CRUD OPERATION (UPDATE) #############
async def update_gpu():
    pass


############# CRUD OPERATION (DELETE) #############
async def delete_gpu(id: str):
    gpu = await get_gpu(id)
    if gpu:
        await gpu_collection.delete_one({"_id": id})
        return True


async def add_price_of_gpu(id: str, price: dict):
    gpu = await get_gpu(id)
    if gpu:
        updated_gpu = await gpu_collection.update_one(
            {"_id": id}, {"$push": {"price_data": price}}
        )
        if updated_gpu:
            return True
        else:
            return False
    else:
        return False
