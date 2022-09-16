from src.mail import (
    read,
    send,
)

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
async def health_check():
    return "pong"
