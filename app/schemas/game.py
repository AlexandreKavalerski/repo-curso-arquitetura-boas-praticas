from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class GameCreate(BaseModel):
    played_at: datetime
    location: Optional[str] = None
    notes: Optional[str] = None


class GameRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    played_at: datetime
    location: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime
