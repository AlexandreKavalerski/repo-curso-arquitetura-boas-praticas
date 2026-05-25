from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.database import SessionLocal
from app.models.player import Player
from app.schemas.player import PlayerCreate, PlayerRead
from app.services import player_service

router = APIRouter(prefix="/players", tags=["players"])


@router.get("/", response_model=list[PlayerRead])
def list_players():
    db: Session = SessionLocal()
    try:
        return db.query(Player).offset(0).limit(100).all()
    finally:
        db.close()


@router.post("/", response_model=PlayerRead, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerCreate):
    db: Session = SessionLocal()
    try:
        player = Player(
            name=player_in.name,
            phone=player_in.phone,
            email=player_in.email,
        )
        db.add(player)
        db.commit()
        db.refresh(player)
        return player
    finally:
        db.close()


@router.get("/{player_id}", response_model=PlayerRead)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = player_service.get_player(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
