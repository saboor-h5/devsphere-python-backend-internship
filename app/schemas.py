from pydantic import BaseModel


class Feature(BaseModel):
    title: str
    description: str


class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str


class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    

class LoginRequest(BaseModel):
    username: str
    password: str


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int