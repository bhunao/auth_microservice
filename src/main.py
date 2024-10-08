import uvicorn

from fastapi import FastAPI
from src.routes import router as user_router

app = FastAPI()

app.include_router(user_router)


@app.get("/")
def home():
    return {"home": "yes"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
