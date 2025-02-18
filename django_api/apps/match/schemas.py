from ninja import Schema
from datetime import datetime


class MatchSchema(Schema):
    id: int
    player1_id: int
    player2_id: int
    status: str
    scheduled_time: datetime
    round_number: int
    score: str
    winner_id: int = None
