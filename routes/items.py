from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

#Item model
class Item(BaseModel):
    nombre: str
    precio: float

# Storage items
items = []

#Create items
@router.post("/", response_model=Item)
def crear_item(item: Item):
    items.append(item)
    return item

#Get items
@router.get("/", response_model=List[Item])
def obtener_items():
    return items