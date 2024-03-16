from pydantic import BaseModel
from typing import List, Optional


class ClubIn(BaseModel):
    name: str
    country: str
    trophies: int


class ClubOut(ClubIn):
    id: int


class ClubUpdate(ClubIn):
    name: Optional[str] = None
    country: Optional[str] = None
    trophies: Optional[int] = None
