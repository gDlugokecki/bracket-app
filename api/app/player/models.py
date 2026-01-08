from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.team.models import Team
    from app.tournament.models import Tournament
    from app.auth.models import User


class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int] = mapped_column(default=1000)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship(back_populates="player")

    tournaments: Mapped[list["Tournament"]] = relationship(secondary="tournament_players", back_populates="players")
    teams: Mapped[list["Team"]] = relationship(secondary="team_players", back_populates="players")
