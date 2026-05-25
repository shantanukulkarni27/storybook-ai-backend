from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

stored_context = []

class ContextRequest(BaseModel):
    contexts: List[str]

@app.get("/")
def root():
    return {
        "message": "Backend running",
        "database": settings.DATABASE_URL
    }

@app.post("/context")
def save_context(data: ContextRequest):
    global stored_context

    stored_context = list(set(stored_context + data.contexts))

    return {
        "success": True,
        "data": stored_context
    }

@app.get("/context")
def get_context():
    return {
        "success": True,
        "data": stored_context
    }