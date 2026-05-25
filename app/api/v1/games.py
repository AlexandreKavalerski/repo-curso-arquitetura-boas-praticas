from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.database import SessionLocal
from app.models.game import Game
from app.schemas.game import GameCreate, GameRead
from app.services import game_service

router = APIRouter(prefix="/games", tags=["games"])


@router.get("/", response_model=list[GameRead])
def list_games():
    db: Session = SessionLocal()
    try:
        return db.query(Game).offset(0).limit(100).all()
    finally:
        db.close()


@router.post("/", response_model=GameRead, status_code=status.HTTP_201_CREATED)
def create_game(game_in: GameCreate):
    db: Session = SessionLocal()
    try:
        game = Game(
            played_at=game_in.played_at,
            location=game_in.location,
            notes=game_in.notes,
        )
        db.add(game)
        db.commit()
        db.refresh(game)
        return game
    finally:
        db.close()


@router.get("/{game_id}", response_model=GameRead)
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = game_service.get_game(db, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game
