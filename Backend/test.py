#testing mongo connection
from pymongo import MongoClient

client = MongoClient("mongodb://172.27.48.1:27017/")
dbnames = client.list_database_names()
print(dbnames)
if 'Planner' in dbnames:
    print ("It's there!")
else:
    #create database
    db = client['Planner']
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

