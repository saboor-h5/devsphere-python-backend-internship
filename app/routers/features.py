from fastapi import APIRouter
from app.models import Feature

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


@router.get("/features")
def get_features():
    return features


@router.post("/features")
def create_feature(feature: Feature):
    return {
        "message": "Feature added successfully.",
        "feature": feature
    }