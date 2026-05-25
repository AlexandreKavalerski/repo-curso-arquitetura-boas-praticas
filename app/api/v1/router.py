from fastapi import APIRouter

from app.api.v1.games import router as games_router
from app.api.v1.groups import router as groups_router
from app.api.v1.players import router as players_router

router = APIRouter()
router.include_router(players_router)
router.include_router(groups_router)
router.include_router(games_router)
