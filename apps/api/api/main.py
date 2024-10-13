from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello from FastAPI backend!"}


