import motor.motor_asyncio
from dotenv import dotenv_values
from .status import return_status
from datetime import datetime

config = dotenv_values(".env")
un = config["MONGO_DB_USERNAME"]
pw = config["MONGO_DB_PASSWORD"]
url = config["MONGO_DB_URL"]

MONGODB_URL = f"mongodb+srv://{un}:{pw}@{url}"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client.gpu_database
gpu_collection = database.get_collection("gpu_collection")


async def get_all_gpus():
    result = []
    async for gpu in gpu_collection.find():
        result.append(gpu)
    return return_status(True, "DB read succeeded.", body=result)


async def update_command(id, command):
    await gpu_collection.update_one({"_id": id}, command)


############# CRUD OPERATION (CREATE) #############
async def add_gpu(data: dict):
    result = await gpu_collection.insert_one(data)
    if not result:
        return return_status(False, "DB insert failed.")
    else:
        await update_command(
            result.inserted_id, {"$set": {"info_last_updated": datetime.now()}}
        )
        return return_status(True, "DB insert succeeded.")


############# CRUD OPERATION (READ) #############
async def get_gpu(id: str):
    result = await gpu_collection.find_one({"_id": id})
    if not result:
        return return_status(False, "DB read failed.")
    else:
        return return_status(True, "DB read succeeded.", body=result)


############# CRUD OPERATION (UPDATE) #############
async def update_gpu(id: str, data: dict):
    result = await gpu_collection.find_one({"_id": id})
    if not result:
        return return_status(False, "DB update failed (item not found).")
    else:
        update_result = await gpu_collection.update_one({"_id": id}, {"$set": data})
        if not update_result:
            return return_status(False, "DB update failed (update failed).")
        else:
            await update_command(id, {"$set": {"info_last_updated": datetime.now()}})
            return return_status(True, "DB update succeeded.")


############# CRUD OPERATION (DELETE) #############
async def delete_gpu(id: str):
    result = await gpu_collection.find_one({"_id": id})
    if not result:
        return return_status(False, "DB delete failed (item not found).")
    else:
        delete_result = await gpu_collection.delete_one({"_id": id})
        if not delete_result:
            return return_status(False, "DB delete failed (delete failed).")
        else:
            return return_status(True, "DB delete succeeded.")


############# CRUD OPERATION (CREATE) #############
async def add_gpu_price(id: str, price: dict):
    result = await gpu_collection.find_one({"_id": id})
    if result:
        updated_gpu = await gpu_collection.update_one(
            {"_id": id}, {"$push": {"price_data": price}}
        )
        if not updated_gpu:
            return return_status(False, "Price insert failed (price not inserted).")
        else:
            await update_command(id, {"$set": {"price_last_updated": datetime.now()}})
            return return_status(True, "Price insert succeeded.")
    else:
        return return_status(False, "Price insert failed (gpu not found).")


############## CRUD OPERATION (READ) #############
async def get_gpu_price(id: str):
    result = await gpu_collection.find_one({"_id": id})
    if not result:
        return return_status(False, "Price read failed (gpu not found).")
    else:
        return return_status(True, "Price read succeeded.", body=result["price_data"])


############## CRUD OPERATION (UPDATE) #############
async def update_gpu_price(id: str, price: dict):
    print(price)
    result = await gpu_collection.find_one({"_id": id})
    if not result:
        return return_status(False, "Price update failed (item not found).")
    else:
        update_result = await gpu_collection.update_one(
            {"_id": id, "price_data.date": price["date"]},
            {"$set": {"price_data.$": price}},
        )
        if not update_result:
            return return_status(False, "Price update failed (update failed).")
        else:
            await update_command(id, {"$set": {"price_last_updated": datetime.now()}})
            return return_status(True, "Price update succeeded.")


############## CRUD OPERATION (DELETE) #############
async def delete_gpu_price(id: str, date: str):
    result = await gpu_collection.find_one({"_id": id})
    if not result:
        return return_status(False, "Price read failed (gpu not found).")
    else:
        delete_result = await gpu_collection.update_one(
            {"_id": id}, {"$pull": {"price_data": {"date": date}}}
        )
        if not delete_result:
            return return_status(False, "Price delete failed (delete failed).")
        else:
            await update_command(id, {"$set": {"price_last_updated": datetime.now()}})
            return return_status(True, "Price delete succeeded.")
