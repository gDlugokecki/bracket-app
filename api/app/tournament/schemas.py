from pydantic import BaseModel, ConfigDict
from datetime import date


class TournamentCreate(BaseModel):
    name: str
    start_date: date
    end_date: date
    location: str
    category: str
    player_ids: list[int] = []


class TournamentUpdate(BaseModel):
    name: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    location: str | None = None
    category: str | None = None


class TournamentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    start_date: date
    end_date: date
    location: str
    category: str
