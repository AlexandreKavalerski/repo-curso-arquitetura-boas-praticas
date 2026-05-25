from sqlalchemy.orm import Session

from app.models.player import Player


def get_player(db: Session, player_id: int) -> Player | None:
    return db.query(Player).filter(Player.id == player_id).first()
