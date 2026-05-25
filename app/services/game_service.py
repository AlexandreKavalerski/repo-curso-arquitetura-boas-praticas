from sqlalchemy.orm import Session

from app.models.game import Game


def get_game(db: Session, game_id: int) -> Game | None:
    return db.query(Game).filter(Game.id == game_id).first()
