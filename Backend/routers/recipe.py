from fastapi import APIRouter, Depends, UploadFile, Form
from typing import Annotated
from .types import Recipe
from ..db.mongodb import getDB
from ..aws.imageUpload import upload_image
from ..common.database import convertBsonToJson
from bson import ObjectId




router = APIRouter(
    prefix="/recipe",
)

@router.get("/")
async def get_recipe(db= Depends(getDB)) -> list:
    """
    Get all recipes from the database.
    """
    # Get all recipes from the database
    db = db['Planner']
    collection = db.get_collection('recipes')
    recipes = await collection.find().to_list(length=100)
    if recipes:
        recipes = convertBsonToJson(recipes)
        recipes = [recipe for recipe in recipes]
        return recipes
    return []
@router.post("/add")
async def add_recipe(recipe: Recipe, db= Depends(getDB) ):
    # Add recipe to database
    print (recipe)
    db = db['Planner']
    collection = db.get_collection('recipes')
    print (recipe.model_dump(exclude={'id'}))
    inserted = await collection.insert_one(recipe.model_dump(exclude={'id'}))
    recipe.id =str(inserted.inserted_id)
    print(recipe)
    return recipe

@router.post("/add/image")
async def add_image(image:UploadFile, recipeId:str = Form(...), type:str = Form(...) ,  db = Depends(getDB)) -> bool:
    """
    Add image to the S3 bucket and put the URL in the database.
    """
    # Add image to S3 bucket
    url = await upload_image(image.file, recipeId, type)
    # Add URL to the database
    db = db['Planner']
    collection = db.get_collection('recipes')
    newValues = await collection.update_one({"_id": ObjectId(recipeId)}, {"$set": {"image": url}})
    print(newValues)
    recipes = await collection.find().to_list(length=100)
    recipes = convertBsonToJson(recipes)
    recipes = [recipe for recipe in recipes]
    print(recipes)
    print(url)
    return True

@router.post("/test")
async def test_image(image: UploadFile ) -> dict:
    print(image.filename)
    return {"filename": image.filename}

    
    
