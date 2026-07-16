from fastapi import APIRouter
from app.models import Feature
from sqlalchemy import text
from app.database import engine

router = APIRouter()

# Temporary in-memory data
features = [
    {
        "id": 1,
        "title": "Fast Performance",
        "description": "High-speed backend APIs."
    },
    {
        "id": 2,
        "title": "Responsive Design",
        "description": "Works on all devices."
    },
    {
        "id": 3,
        "title": "Easy Integration",
        "description": "Simple REST API integration."
    }
]



@router.post("/features")
def create_feature(feature: Feature):

    with engine.begin() as connection:
        connection.execute(
            text("""
                INSERT INTO features(title, description)
                VALUES (:title, :description)
            """),
            {
                "title": feature.title,
                "description": feature.description
            }
        )

    return {
        "message": "Feature added successfully.",
        "feature": feature
    }


@router.get("/features")
def get_features():
    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT * FROM features")
        )

        rows = result.mappings().all()

    return rows
