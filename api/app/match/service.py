from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.player.models import Player
from app.team.models import Team
from app.match.models import Match
from app.match.schemas import MatchCreate, MatchUpdate


async def get_match_by_id(db: AsyncSession, match_id: int) -> Optional[Match]:
    result = await db.execute(
        select(Match)
        .options(
            selectinload(Match.team1).selectinload(Team.players),
            selectinload(Match.team2).selectinload(Team.players),
            selectinload(Match.winner_team),
            selectinload(Match.tournament),
        )
        .where(Match.id == match_id)
    )
    return result.scalar_one_or_none()


async def get_all_matches(
    db: AsyncSession, tournament_id: Optional[int] = None, skip: int = 0, limit: int = 100
) -> list[Match]:
    query = select(Match).options(
        selectinload(Match.team1).selectinload(Team.players),
        selectinload(Match.team2).selectinload(Team.players),
        selectinload(Match.winner_team),
        selectinload(Match.tournament),
    )

    if tournament_id is not None:
        query = query.where(Match.tournament_id == tournament_id)

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)
    return list(result.scalars().all())


async def create_match(db: AsyncSession, match_data: MatchCreate) -> Match:
    result = await db.execute(
        select(Player).where(Player.id.in_([*match_data.team1_player_ids, *match_data.team2_player_ids]))
    )
    players = list(result.scalars().all())

    team1_players = [p for p in players if p.id in match_data.team1_player_ids]
    team2_players = [p for p in players if p.id in match_data.team2_player_ids]

    combined_players = [*match_data.team1_player_ids, *match_data.team2_player_ids]

    if len(players) != len(combined_players):
        founds_ids = {p.id for p in players}
        missing_ids = set(combined_players) - founds_ids
        raise ValueError(f"Players not found: {missing_ids}")

    if len(combined_players) not in [2, 4]:
        raise ValueError("Must provide 2 players (singles) or 4 players (doubles)")

    team1 = Team(players=team1_players)
    team2 = Team(players=team2_players)

    match = Match(
        tournament_id=match_data.tournament_id,
        team1=team1,
        team2=team2,
        scheduled_time=match_data.scheduled_time,
        court_number=match_data.court_number,
        round_number=match_data.round_number,
    )

    db.add(match)

    try:
        await db.commit()
        await db.refresh(match)
    except Exception as e:
        await db.rollback()
        raise e

    return match


async def update_match(db: AsyncSession, match_id: int, match_data: MatchUpdate) -> Match:
    result = await db.execute(
        select(Match)
        .options(
            selectinload(Match.team1).selectinload(Team.players),
            selectinload(Match.team2).selectinload(Team.players),
            selectinload(Match.winner_team),
            selectinload(Match.tournament),
        )
        .where(Match.id == match_id)
    )
    match = result.scalar_one_or_none()
    if not match:
        raise ValueError("Match not found")

    update_dict = match_data.model_dump(exclude_unset=True)

    for key, value in update_dict.items():
        setattr(match, key, value)
    try:
        await db.commit()
        await db.refresh(match)
    except Exception as e:
        await db.rollback()
        raise e

    return match


async def delete_match(db: AsyncSession, match_id: int) -> bool:
    result = await db.execute(select(Match).where(Match.id == match_id))
    match = result.scalar_one_or_none()

    if not match:
        raise ValueError("Match not found")

    await db.delete(match)

    try:
        await db.commit()
    except Exception as e:
        await db.rollback()
        raise e

    return True
