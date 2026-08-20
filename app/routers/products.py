from fastapi import APIRouter, HTTPException, Depends
from app.schemas import ProductCreate, ProductUpdate, ProductOut
from app.crud import products as product_crud
from app.dependencies import get_current_user


router = APIRouter()


@router.post("/products")
def create_product(
    product: ProductCreate,
    current_user: dict = Depends(get_current_user)
):
    product_id = product_crud.create_product(product, created_by=current_user["id"])
    return {
        "message": "Product created successfully!",
        "id": product_id
    }


@router.get("/products", response_model=list[ProductOut])
def get_products():
    return product_crud.get_products()



@router.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int):
    product = product_crud.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product


@router.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductUpdate,
    current_user: dict = Depends(get_current_user)
):
    existing = product_crud.get_product(product_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Product not found.")

    rowcount = product_crud.update_product(product_id, product, current_user["id"])
    if rowcount == 0:
        raise HTTPException(status_code=403, detail="You do not have permission to update this product.")

    return {"message": "Product updated successfully.", "id": product_id}


@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    current_user: dict = Depends(get_current_user)
):
    existing = product_crud.get_product(product_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Product not found.")

    rowcount = product_crud.delete_product(product_id, current_user["id"])
    if rowcount == 0:
        raise HTTPException(status_code=403, detail="You do not have permission to delete this product.")

    return {"message": "Product deleted successfully.", "id": product_id}