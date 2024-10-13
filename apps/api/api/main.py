from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Sample data
items = [
    {"id": str(uuid.uuid4()), "title": "Item 1"},
    {"id": str(uuid.uuid4()), "title": "Item 2"},
    {"id": str(uuid.uuid4()), "title": "Item 3"},
]

class Item(BaseModel):
    id: str
    title: str

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI backend!"}

@app.get("/items", response_model=List[Item])
async def get_items():
    return items

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: str):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, updated_item: Item):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items[index] = updated_item.dict()
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            del items[index]
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")