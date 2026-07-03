"""MongoDB connection manager."""

from __future__ import annotations

from typing import Any

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import PyMongoError

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


class MongoManager:
    """Manage the application's MongoDB connection."""

    def __init__(self) -> None:
        self._client: MongoClient[dict[str, Any]] | None = None
        self._database: Database[dict[str, Any]] | None = None

    @property
    def client(self) -> MongoClient[dict[str, Any]]:
        """Return the MongoDB client."""
        if self._client is None:
            raise RuntimeError("MongoDB client has not been initialized.")
        return self._client

    @property
    def database(self) -> Database[dict[str, Any]]:
        """Return the application database."""
        if self._database is None:
            raise RuntimeError("MongoDB database has not been initialized.")
        return self._database

    def connect(self) -> None:
        """Create the MongoDB connection."""
        if self._client is not None:
            logger.warning("MongoDB client is already initialized.")
            return

        logger.info("Connecting to MongoDB...")

        try:
            client: MongoClient[dict[str, Any]] = MongoClient(
                settings.mongo_uri,
                serverSelectionTimeoutMS=5000,
            )

            client.admin.command("ping")

            database = self._get_database(client)

            self._client = client
            self._database = database

            logger.info("MongoDB connection established.")

        except PyMongoError:
            logger.exception("Failed to connect to MongoDB.")
            raise

        if not settings.mongo_database:
            raise ValueError("MONGO_DATABASE is not set")

    def disconnect(self) -> None:
        """Close the MongoDB connection."""
        if self._client is None:
            logger.warning("MongoDB client already closed.")
            return

        logger.info("Closing MongoDB connection...")

        self._client.close()

        self._client = None
        self._database = None

        logger.info("MongoDB connection closed.")

    def _get_database(
        self,
        client: MongoClient[dict[str, Any]],
    ) -> Database[dict[str, Any]]:
        """Return the configured MongoDB database."""

        if not settings.mongo_database:
            raise ValueError("MONGO_DATABASE is not configured.")

        return client[settings.mongo_database]


mongo_manager = MongoManager()
