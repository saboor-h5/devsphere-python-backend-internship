from pydantic import BaseModel


class Feature(BaseModel):
    title: str
    description: str


class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str
