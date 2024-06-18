from motor.motor_asyncio import AsyncIOMotorClient

async def getDb():
    """
    Returns a database connection

    """
    client = AsyncIOMotorClient("mongodb://172.27.48.1:27017/")
    return client
   

        