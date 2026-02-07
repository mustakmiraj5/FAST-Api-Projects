from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

load_dotenv()

# Create FastAPI app instance
app = FastAPI(title=os.getenv("APP_NAME", "FastAPI Application"))


@app.get("/ping")
def ping():
    return JSONResponse(content={"message": "pong!", "status": "success"})

@app.get("/greet/{name}")
def greet(name: str):
    return JSONResponse(content={"message": f"Hello, {name}!", "status": "success"})
