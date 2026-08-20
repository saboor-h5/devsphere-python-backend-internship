from fastapi import APIRouter, Depends, HTTPException
from app.schemas import User, UserUpdate, LoginRequest, UserOut
from app.crud import users as user_crud
from app.security import verify_password
from app.jwt_handler import create_access_token
from app.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register")
def register(user: User):
    user_id = user_crud.create_user(user)
    return {
        "message": "User registered successfully",
        "id": user_id,
        "username": user.username
    }


@router.post("/login")
def login(user: OAuth2PasswordRequestForm = Depends()):
    db_user = user_crud.get_user_by_username(user.username)

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    access_token = create_access_token({
        "sub": user.username,
        "id": db_user["id"]
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, current_user: dict = Depends(get_current_user)):
    user = user_crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user


@router.put("/{user_id}")
def update_user(
    user_id: int,
    user: UserUpdate,
    current_user: dict = Depends(get_current_user)
):
    rowcount = user_crud.update_user(user_id, user)
    if rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": "User updated successfully.", "id": user_id}


@router.delete("/{user_id}")
def delete_user(user_id: int, current_user: dict = Depends(get_current_user)):
    rowcount = user_crud.delete_user(user_id)
    if rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": "User deleted successfully.", "id": user_id}