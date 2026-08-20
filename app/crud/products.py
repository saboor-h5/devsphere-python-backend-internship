from sqlalchemy import text
from app.database import engine


def create_product(product, created_by: int):
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                INSERT INTO products
                (name, description, price, quantity, created_by)
                VALUES
                (:name, :description, :price, :quantity, :created_by)
            """),
            {
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "quantity": product.quantity,
                "created_by": created_by
            }
        )
        connection.commit()
        return result.lastrowid


def get_products():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM products"))
        return result.mappings().all()


def get_product(product_id: int):
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT * FROM products
                WHERE id = :product_id
            """),
            {"product_id": product_id}
        )
        return result.mappings().first()


def update_product(product_id: int, product, user_id: int):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                UPDATE products
                SET name = :name,
                    description = :description,
                    price = :price,
                    quantity = :quantity
                WHERE id = :product_id AND created_by = :user_id
            """),
            {
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "quantity": product.quantity,
                "product_id": product_id,
                "user_id": user_id
            }
        )
        return result.rowcount


def delete_product(product_id: int, user_id: int):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                DELETE FROM products
                WHERE id = :product_id AND created_by = :user_id
            """),
            {"product_id": product_id, "user_id": user_id}
        )
        return result.rowcount