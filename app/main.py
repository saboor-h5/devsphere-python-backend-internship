from fastapi import FastAPI, Request, Header, HTTPException, Depends
from app.routers.features import router as features_router
from app.routers.users import router as users_router
from app.routers.products import router as products_router
from app.jwt_handler import verify_access_token
from app.dependencies import get_current_user

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


@app.get("/profile")
def profile(
    current_user: dict = Depends(get_current_user)
):
    return {
        "message": "Welcome",
        "user": current_user["sub"]
    }

app.include_router(features_router)
app.include_router(users_router)
app.include_router(products_router)