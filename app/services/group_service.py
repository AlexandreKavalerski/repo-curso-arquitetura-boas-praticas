from sqlalchemy.orm import Session

from app.models.group import Group


def get_group(db: Session, group_id: int) -> Group | None:
    return db.query(Group).filter(Group.id == group_id).first()
