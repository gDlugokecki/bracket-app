from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
import enum


if TYPE_CHECKING:
    from app.team.models import Team
    from app.tournament.models import Tournament


class MatchStatus(str, enum.Enum):
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"


class Match(Base):
    __tablename__ = "matches"
    id: Mapped[int] = mapped_column(primary_key=True)

    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournaments.id"))
    team1_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    team2_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    winner_team_id: Mapped[int | None] = mapped_column(ForeignKey("teams.id"))

    status: Mapped[MatchStatus] = mapped_column(default=MatchStatus.SCHEDULED)

    scheduled_time: Mapped[datetime]
    court_number: Mapped[str | None]
    round_number: Mapped[int | None]

    score: Mapped[str | None]
    duration: Mapped[timedelta | None]

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )

    team1: Mapped["Team"] = relationship(back_populates="matches_as_team1", foreign_keys=[team1_id])
    team2: Mapped["Team"] = relationship(back_populates="matches_as_team2", foreign_keys=[team2_id])
    winner_team: Mapped["Team | None"] = relationship(back_populates="matches_won", foreign_keys=[winner_team_id])
    tournament: Mapped["Tournament"] = relationship(back_populates="matches")
