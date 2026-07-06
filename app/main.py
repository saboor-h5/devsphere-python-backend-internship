from fastapi import FastAPI
from app.routers.features import router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server Running!"}


@app.get("/about")
def about():
    return {"message": "This backend server is built using FastAPI."}


app.include_router(router)  