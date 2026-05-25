from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PlayerCreate(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None


class PlayerRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime
    updated_at: datetime
