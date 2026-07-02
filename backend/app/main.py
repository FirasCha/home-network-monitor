from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import get_logger, setup_logging

setup_logging()

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    logger.info("Starting %s v%s", settings.app_name, settings.app_version)

    yield

    logger.info("Stopping application")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)


@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    logger.debug("Health endpoint called")

    return {"status": "ok"}
