from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    return response


@app.get("/")
def home():
    return {"message": "Server Running"}


@app.get("/about")
def about():
    return {
        "message": "This backend server is built using FastAPI."
    }