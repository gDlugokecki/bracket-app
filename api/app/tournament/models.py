from datetime import date
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.player.models import Player
    from app.match.models import Match


tournament_players = Table(
    "tournament_players",
    Base.metadata,
    Column("tournament_id", ForeignKey("tournaments.id"), primary_key=True),
    Column("player_id", ForeignKey("players.id"), primary_key=True),
)


class Tournament(Base):
    __tablename__ = "tournaments"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    start_date: Mapped[date]
    end_date: Mapped[date]
    location: Mapped[str] = mapped_column(String(200))
    category: Mapped[str] = mapped_column(String(50))

    players: Mapped[list["Player"]] = relationship(secondary=tournament_players, back_populates="tournaments")
    matches: Mapped[list["Match"]] = relationship(back_populates="tournament")
