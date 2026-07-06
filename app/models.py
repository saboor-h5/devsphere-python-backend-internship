from pydantic import BaseModel


class Feature(BaseModel):
    title: str
    description: str