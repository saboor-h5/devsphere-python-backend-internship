from pydantic import BaseModel, Field, field_validator


class Feature(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)


class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=8)

    @field_validator("username")
    @classmethod
    def username_no_spaces(cls, value):
        if " " in value:
            raise ValueError("Username cannot contain spaces.")
        return value


class UserUpdate(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)


class LoginRequest(BaseModel):
    username: str
    password: str


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)


class ProductUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)



class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    created_by: int

    class Config:
        from_attributes = True


class FeatureOut(BaseModel):
    id: int
    title: str
    description: str
    created_by: int

    class Config:
        from_attributes = True


class UserOut(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str

    class Config:
        from_attributes = True