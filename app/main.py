from contextlib import asynccontextmanager

from fastapi import FastAPI

import app.models  # noqa: F401 — registers all ORM models with Base
from app.api.v1.router import router as api_router
from app.core.database import engine
from app.core.settings import settings
from app.models.base import Base


@asynccontextmanager
async def lifespan(application: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)
app.include_router(api_router, prefix="/api/v1")
