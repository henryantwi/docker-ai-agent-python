import os

from fastapi import FastAPI

app = FastAPI()

API_KEY = os.getenv("API_KEY")
MY_PROJECT = os.getenv("MY_PROJECT") or "Something else"

@app.get("/")
def read_root():
    return {
        "message": "Hello, World Again!",
        "MY_PROJECT": MY_PROJECT,
        "API_KEY": API_KEY,
    }