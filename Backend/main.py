from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routers.recipe import router
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from .db.mongodbUtils import connectToMongo, closeMongo

@asynccontextmanager
async def lifespan(app: FastAPI):
    dbClient = AsyncIOMotorClient("mongodb://172.27.48.1:27017/")
    dbNames = await dbClient.list_database_names()
    if 'Planner' not in dbNames:

        #create database
        db = dbClient['Planner']
        #create collection
        collection = db['users']
        #insert user from env variables TODO: change to env variables
        user = {
            "username": "admin",
            "password": "admin"
        }
        collection.insert_one(user)

        print("User inserted")
        print("Database created")
    
    dbClient.close()
    await connectToMongo()
    yield
    await closeMongo()
app = FastAPI(lifespan=lifespan)
orgins = [
    'http://localhost:8081',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)