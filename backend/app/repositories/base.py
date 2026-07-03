"""Base repository implementation."""

from __future__ import annotations

from typing import Any

from pymongo.collection import Collection
from pymongo.database import Database


class BaseRepository:
    """Base class for MongoDB repositories."""

    def __init__(
        self,
        database: Database[dict[str, Any]],
        collection_name: str,
    ) -> None:
        self._database = database
        self._collection: Collection[dict[str, Any]] = database[collection_name]

    @property
    def collection(self) -> Collection[dict[str, Any]]:
        """Return the MongoDB collection."""
        return self._collection
