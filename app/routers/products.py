from fastapi import APIRouter, HTTPException
from app.schemas import ProductCreate, ProductUpdate
from app.crud import products as product_crud

router = APIRouter()


@router.post("/products")
def create_product(product: ProductCreate):
    product_id = product_crud.create_product(product)
    return {
        "message": "Product created successfully!",
        "id": product_id
    }


@router.get("/products")
def get_products():
    return product_crud.get_products()


@router.get("/products/{product_id}")
def get_product(product_id: int):
    product = product_crud.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product


@router.put("/products/{product_id}")
def update_product(product_id: int, product: ProductUpdate):
    rowcount = product_crud.update_product(product_id, product)
    if rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found.")
    return {"message": "Product updated successfully.", "id": product_id}


@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    rowcount = product_crud.delete_product(product_id)
    if rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found.")
    return {"message": "Product deleted successfully.", "id": product_id}