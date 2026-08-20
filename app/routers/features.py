from fastapi import APIRouter, HTTPException, Depends
from app.schemas import Feature, FeatureOut
from app.crud import features as feature_crud
from app.dependencies import get_current_user


router = APIRouter()


@router.post("/features")
def create_feature(
    feature: Feature,
    current_user: dict = Depends(get_current_user)
):
    feature_id = feature_crud.create_feature(feature, created_by=current_user["id"])
    return {
        "message": "Feature added successfully.",
        "id": feature_id
    }


@router.get("/features", response_model=list[FeatureOut])
def get_features():
    return feature_crud.get_features()


@router.get("/features/{feature_id}", response_model=FeatureOut)
def get_feature(feature_id: int):
    feature = feature_crud.get_feature(feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found.")
    return feature


@router.put("/features/{feature_id}")
def update_feature(
    feature_id: int,
    feature: Feature,
    current_user: dict = Depends(get_current_user)
):
    existing = feature_crud.get_feature(feature_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Feature not found.")

    rowcount = feature_crud.update_feature(feature_id, feature, current_user["id"])
    if rowcount == 0:
        raise HTTPException(status_code=403, detail="You do not have permission to update this feature.")

    return {"message": "Feature updated successfully.", "id": feature_id}


@router.delete("/features/{feature_id}")
def delete_feature(
    feature_id: int,
    current_user: dict = Depends(get_current_user)
):
    existing = feature_crud.get_feature(feature_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Feature not found.")

    rowcount = feature_crud.delete_feature(feature_id, current_user["id"])
    if rowcount == 0:
        raise HTTPException(status_code=403, detail="You do not have permission to delete this feature.")

    return {"message": "Feature deleted successfully.", "id": feature_id}