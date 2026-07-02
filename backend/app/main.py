from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import get_logger, setup_logging
from app.db.mongodb import mongo_manager

setup_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting application...")

    try:
        mongo_manager.connect()
        logger.info("MongoDB connected successfully")
    except Exception as e:
        logger.critical(f"Failed to connect to MongoDB: {e}")
        raise

    yield

    # Shutdown
    logger.info("Shutting down application...")
    mongo_manager.disconnect()
    logger.info("Shutdown complete")


app = FastAPI(lifespan=lifespan)


@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    logger.debug("Health endpoint called")
    return {"status": "ok"}
