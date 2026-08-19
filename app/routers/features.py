from fastapi import APIRouter, HTTPException
from app.schemas import Feature
from app.crud import features as feature_crud

router = APIRouter()


@router.post("/features")
def create_feature(feature: Feature):
    feature_id = feature_crud.create_feature(feature)
    return {
        "message": "Feature added successfully.",
        "id": feature_id
    }


@router.get("/features")
def get_features():
    return feature_crud.get_features()


@router.get("/features/{feature_id}")
def get_feature(feature_id: int):
    feature = feature_crud.get_feature(feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found.")
    return feature


@router.put("/features/{feature_id}")
def update_feature(feature_id: int, feature: Feature):
    rowcount = feature_crud.update_feature(feature_id, feature)
    if rowcount == 0:
        raise HTTPException(status_code=404, detail="Feature not found.")
    return {"message": "Feature updated successfully.", "id": feature_id}


@router.delete("/features/{feature_id}")
def delete_feature(feature_id: int):
    rowcount = feature_crud.delete_feature(feature_id)
    if rowcount == 0:
        raise HTTPException(status_code=404, detail="Feature not found.")
    return {"message": "Feature deleted successfully.", "id": feature_id}