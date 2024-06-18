from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()

async def getDB() -> AsyncIOMotorClient:
    return db.client