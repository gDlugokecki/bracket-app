from datetime import date

from app.schemas import CamelCaseModel


class TournamentCreate(CamelCaseModel):
    name: str
    start_date: date
    end_date: date
    location: str
    category: str
    player_ids: list[int] = []


class TournamentUpdate(CamelCaseModel):
    name: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    location: str | None = None
    category: str | None = None


class TournamentResponse(CamelCaseModel):

    id: int
    name: str
    start_date: date
    end_date: date
    location: str
    category: str
