"""Database dependencies."""

from typing import Any

from pymongo.database import Database

from app.db.mongodb import mongo_manager


def get_database() -> Database[dict[str, Any]]:
    """Return the application MongoDB database instance."""
    return mongo_manager.database
