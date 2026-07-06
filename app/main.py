from fastapi import FastAPI, Request
from app.routers.features import router as features_router

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"{request.method} {request.url}")
    response = await call_next(request)
    return response


@app.get("/")
def root():
    return {"message": "Server Running!"}


@app.get("/about")
def about():
    return {"message": "This backend server is built using FastAPI."}


app.include_router(features_router)