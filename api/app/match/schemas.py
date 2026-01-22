from datetime import datetime, timedelta
from typing import Any

from pydantic import field_validator, model_validator

from app.match.models import MatchStatus
from app.player.schemas import PlayerResponse
from app.schemas import CamelCaseModel


class MatchCreate(CamelCaseModel):
    tournament_id: int
    is_double: bool
    team1_player_ids: list[int]
    team2_player_ids: list[int]
    scheduled_time: datetime
    court_number: str
    round_number: int

    @field_validator("team1_player_ids", "team2_player_ids")
    def validate_team_size(cls, value):
        if len(value) not in [1, 2]:
            raise ValueError("Each team must have 1 or 2 players")
        return value


class MatchResponse(CamelCaseModel):
    id: int
    tournament_id: int
    team1_id: int
    team2_id: int
    winner_team_id: int | None

    status: MatchStatus
    scheduled_time: datetime
    court_number: str | None
    round_number: int | None

    score: str | None
    duration: timedelta | None

    created_at: datetime
    updated_at: datetime

    # Team player data
    team1_players: list[PlayerResponse] = []
    team2_players: list[PlayerResponse] = []

    @model_validator(mode="before")
    @classmethod
    def extract_team_players(cls, data: Any) -> Any:
        # If data is a Match model instance, extract players from teams
        if hasattr(data, "team1") and hasattr(data, "team2"):
            if hasattr(data.team1, "players"):
                data.team1_players = data.team1.players
            if hasattr(data.team2, "players"):
                data.team2_players = data.team2.players
        return data


class MatchUpdate(CamelCaseModel):
    status: MatchStatus | None = None
    winner_team_id: int | None = None
    score: str | None = None
    duration: timedelta | None = None
    scheduled_time: datetime | None = None
    court_number: str | None = None
    round_number: int | None = None
