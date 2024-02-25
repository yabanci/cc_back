from fastapi import FastAPI
from app.views import view


app = FastAPI()

app.include_router(view.router)


@app.get("/ping")
async def root():
    return {"message": "I am alive"}
