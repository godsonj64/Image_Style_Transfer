import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.health import router as health_router
from app.api.tasks import router as tasks_router
from app.config import get_settings
from app.storage.db import init_db
from app.telemetry.logger import configure_logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    settings = get_settings()
    configure_logging()
    init_db(str(settings.sqlite_path))
    logger.info("application_started", extra={"event": {"sqlite_path": str(settings.sqlite_path)}})
    yield


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)
    app.include_router(health_router)
    app.include_router(tasks_router)

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        logger.exception("unhandled_exception", extra={"event": {"path": str(request.url.path)}})
        return JSONResponse(status_code=500, content={"detail": "internal_server_error"})

    return app


app = create_app()
