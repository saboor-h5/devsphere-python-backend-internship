from fastapi import APIRouter, Depends
from sqlalchemy import text
from app.models import User, LoginRequest
from app.database import engine
from app.security import hash_password, verify_password
from app.jwt_handler import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

import app

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register")
def register(user: User):

    hashed_password = hash_password(user.password)

    with engine.connect() as connection:
        connection.execute(
            text("""
                INSERT INTO users
                (username, first_name, last_name, password)
                VALUES
                (:username, :first_name, :last_name, :password)
            """),
            {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "password": hashed_password
            }
        )

        connection.commit()
        
    return {
        "message": "User registered successfully",
        "user": user
    }


@router.post("/login")
def login(user: OAuth2PasswordRequestForm = Depends()):

    with engine.connect() as connection:

        result = connection.execute(
            text(
                """
                SELECT * 
                FROM users
                WHERE username = :username
                """
            ),
            {"username": user.username}
        )

        db_user = result.mappings().first()
        if not db_user:
            return {"message": "Invalid username or password."}

        if not verify_password(
            user.password,
            db_user["password"]
        ):
            return {"message": "Invalid username or password"}

        access_token = create_access_token(
            {"sub": user.username}
        )

        return{
            "access_token": access_token,
            "token_type": "bearer"
        }
