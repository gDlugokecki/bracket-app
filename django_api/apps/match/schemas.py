from ninja import ModelSchema, Schema
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from .models import Match
from apps.player.models import Player


class BaseConfig(Schema):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class PlayerSchema(ModelSchema, BaseConfig):
    class Meta:
        model = Player
        fields = ["id", "first_name", "last_name"]

    # WORKAROUND https://github.com/vitalik/django-ninja/issues/828
    id: int


class MatchSchema(ModelSchema, BaseConfig):
    class Meta:
        model = Match
        fields = [
            "id",
            "status",
            "scheduled_time",
            "round_number",
            "score",
        ]

    player_1: PlayerSchema
    player_2: PlayerSchema
    winner_id: int | None
