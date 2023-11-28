from fastapi import FastAPI
from app import app
import uvicorn

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)