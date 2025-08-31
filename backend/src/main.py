import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.db import init_db
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

API_KEY = os.getenv("API_KEY")

@app.get("/")
def read_root():
    return {
        "message": "Hello, World!",
    }
    
@app.get("/health/")
def health_check():
    return {"status": "ok"}

app.include_router(chat_router, prefix="/api")
