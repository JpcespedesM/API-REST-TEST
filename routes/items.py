from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

#Item model
class ItemCreate(BaseModel):
    nombre: str
    precio: float

#item model with id
class Item(ItemCreate):
    id: str

#Storage items
items = []

#Create items
@router.post("/", response_model=Item)
def crear_item(item: ItemCreate):
    nuevo_item = Item(
        id=str(uuid.uuid4()),
        nombre=item.nombre,
        precio=item.precio
    )
    items.append(nuevo_item)
    return nuevo_item

#Get items
@router.get("/", response_model=List[Item])
def obtener_items():
    return items

@router.get("/{item_id}", response_model=Item)
def obtener_item_por_id(item_id: str):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")