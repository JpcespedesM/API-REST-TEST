from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

# Modelo para los items
class Item(BaseModel):
    id: str
    nombre: str
    precio: float

# Lista en memoria para almacenar los items
items = []

#Create items
@router.post("/", response_model=Item)
def crear_item(item: Item):
    # Generar un ID único para el nuevo item
    item.id = str(uuid.uuid4())
    items.append(item)
    return item

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