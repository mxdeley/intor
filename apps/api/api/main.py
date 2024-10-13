from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

# In-memory database
db = []

class Item(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI backend!"}

@app.post("/items", response_model=Item)
async def create_item(item: ItemCreate):
    new_item = Item(id=str(uuid.uuid4()), **item.dict())
    db.append(new_item)
    return new_item

@app.get("/items", response_model=List[Item])
async def read_items():
    return db

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    item = next((item for item in db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: ItemCreate):
    existing_item = next((item for item in db if item.id == item_id), None)
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    existing_item.name = item.name
    existing_item.description = item.description
    return existing_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    global db
    db = [item for item in db if item.id != item_id]
    return {"message": "Item deleted successfully"}
