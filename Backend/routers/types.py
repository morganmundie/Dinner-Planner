from pydantic import BaseModel
from typing import Union, Optional

class Recipe(BaseModel):
    id: Optional[str]= None
    name: str
    ingredients: str
    instructions: str