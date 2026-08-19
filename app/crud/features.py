from sqlalchemy import text
from app.database import engine


def create_feature(feature):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                INSERT INTO features(title, description)
                VALUES (:title, :description)
            """),
            {
                "title": feature.title,
                "description": feature.description
            }
        )
        return result.lastrowid


def get_features():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM features"))
        return result.mappings().all()


def get_feature(feature_id: int):
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT * FROM features
                WHERE id = :feature_id
            """),
            {"feature_id": feature_id}
        )
        return result.mappings().first()


def update_feature(feature_id: int, feature):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                UPDATE features
                SET title = :title,
                    description = :description
                WHERE id = :feature_id
            """),
            {
                "title": feature.title,
                "description": feature.description,
                "feature_id": feature_id
            }
        )
        return result.rowcount


def delete_feature(feature_id: int):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                DELETE FROM features
                WHERE id = :feature_id
            """),
            {"feature_id": feature_id}
        )
        return result.rowcount