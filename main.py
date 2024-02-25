import uvicorn
from fastapi import FastAPI

from app.views import view

app = FastAPI()

app.include_router(view.router)


@app.get("/ping")
async def root():
    return {"message": "I am alive"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)
