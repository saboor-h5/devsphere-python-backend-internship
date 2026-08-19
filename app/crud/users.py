from sqlalchemy import text
from app.database import engine
from app.security import hash_password


def create_user(user):
    hashed_password = hash_password(user.password)

    with engine.begin() as connection:
        result = connection.execute(
            text("""
                INSERT INTO users
                (username, first_name, last_name, password)
                VALUES
                (:username, :first_name, :last_name, :password)
            """),
            {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "password": hashed_password
            }
        )
        return result.lastrowid


def get_user_by_username(username: str):
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT * FROM users
                WHERE username = :username
            """),
            {"username": username}
        )
        return result.mappings().first()


def get_user(user_id: int):
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT id, username, first_name, last_name
                FROM users
                WHERE id = :user_id
            """),
            {"user_id": user_id}
        )
        return result.mappings().first()


def update_user(user_id: int, user):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                UPDATE users
                SET first_name = :first_name,
                    last_name = :last_name
                WHERE id = :user_id
            """),
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_id": user_id
            }
        )
        return result.rowcount


def delete_user(user_id: int):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                DELETE FROM users
                WHERE id = :user_id
            """),
            {"user_id": user_id}
        )
        return result.rowcount