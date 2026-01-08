from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


if TYPE_CHECKING:
    from app.player.models import Player
    from app.match.models import Match

team_players = Table(
    "team_players",
    Base.metadata,
    Column("team_id", ForeignKey("teams.id"), primary_key=True),
    Column("player_id", ForeignKey("players.id"), primary_key=True),
)


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None]

    players: Mapped[list["Player"]] = relationship(secondary=team_players, back_populates="teams")
    matches_as_team1: Mapped[list["Match"]] = relationship(back_populates="team1", foreign_keys="Match.team1_id")
    matches_as_team2: Mapped[list["Match"]] = relationship(back_populates="team2", foreign_keys="Match.team2_id")
    matches_won: Mapped[list["Match"]] = relationship(back_populates="winner_team", foreign_keys="Match.winner_team_id")
