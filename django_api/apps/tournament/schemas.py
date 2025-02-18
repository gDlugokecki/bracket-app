from ninja import ModelSchema
from datetime import date
from typing import List
from .models import Tournament
from apps.player.models import Player


class PlayerSchema(ModelSchema):
    class Config:
        model = Player
        model_fields = [
            "id",
            "first_name",
            "last_name",
        ]


class TournamentSchema(ModelSchema):
    players: List[PlayerSchema]

    class Config:
        model = Tournament
        model_fields = [
            "id",
            "name",
            "start_date",
            "end_date",
            "location",
            "category",
            "players",
        ]


class TournamentListSchema(ModelSchema):
    class Config:
        model = Tournament
        model_fields = ["id", "name", "start_date", "end_date", "location", "category"]
