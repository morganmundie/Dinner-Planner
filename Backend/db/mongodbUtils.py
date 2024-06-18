from motor.motor_asyncio import AsyncIOMotorClient

from .mongodb import db

async def connectToMongo():
    print("went")
    db.client = AsyncIOMotorClient("mongodb://172.27.48.1:27017/")
    print(db)

async def closeMongo():
    db.client.close()
