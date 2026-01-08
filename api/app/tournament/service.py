from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.player.models import Player
from app.player.service import get_player_by_id
from app.tournament.schemas import TournamentCreate, TournamentResponse, TournamentUpdate
from app.tournament.models import Tournament


async def create_tournament(db: AsyncSession, tournament_data: TournamentCreate) -> Tournament:
    tournament_dict = tournament_data.model_dump(exclude={"player_ids"})

    tournament = Tournament(**tournament_dict)
    db.add(tournament)

    if tournament_data.player_ids:
        result = await db.execute(select(Player).where(Player.id.in_(tournament_data.player_ids)))
        players = list(result.scalars().all())

        if len(players) != len(tournament_data.player_ids):
            found_ids = {p.id for p in players}
            missing_ids = set(tournament_data.player_ids) - found_ids
            raise ValueError(f"Players not found: {missing_ids}")

        tournament.players = players

    try:
        await db.commit()
        await db.refresh(tournament)
    except Exception as e:
        await db.rollback()
        raise e

    return tournament


async def get_tournament_by_id(db: AsyncSession, tournament_id: int) -> Optional[Tournament]:
    result = await db.execute(
        select(Tournament).options(selectinload(Tournament.players)).where(Tournament.id == tournament_id)
    )
    return result.scalar_one_or_none()


async def get_all_tournaments(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Tournament]:
    result = await db.execute(select(Tournament).options(selectinload(Tournament.players)).offset(skip).limit(limit))
    return list(result.scalars().all())


async def delete_tournament(db: AsyncSession, tournament_id: int) -> bool:
    tournament = await get_tournament_by_id(db, tournament_id)

    if not tournament:
        raise ValueError("Tournament not found")

    await db.delete(tournament)

    try:
        await db.commit()
    except Exception as e:
        await db.rollback()
        raise e

    return True


async def add_player_to_tournament(db: AsyncSession, tournament_id: int, player_id: int) -> Tournament:
    player = await get_player_by_id(db, player_id)
    if not player:
        raise ValueError("Player not found")

    tournament = await get_tournament_by_id(db, tournament_id)
    if not tournament:
        raise ValueError("Tournament not found")

    tournament.players.append(player)

    try:
        await db.commit()
        await db.refresh(tournament)
    except Exception as e:
        await db.rollback()
        raise e

    return tournament


async def remove_player_from_tournament(db: AsyncSession, tournament_id: int, player_id: int) -> bool:
    player = await get_player_by_id(db, player_id)
    if not player:
        raise ValueError("Player not found")

    tournament = await get_tournament_by_id(db, tournament_id)
    if not tournament:
        raise ValueError("Tournament not found")

    tournament.players.remove(player)

    try:
        await db.commit()
        await db.refresh(tournament)
    except Exception as e:
        await db.rollback()
        raise e

    return True


async def get_tournament_players(db: AsyncSession, tournament_id: int) -> list[Player]:
    tournament = await get_tournament_by_id(db, tournament_id)
    if not tournament:
        raise ValueError("Tournament not found")

    players_list = tournament.players

    return players_list


async def update_tournament(
    db: AsyncSession, tournament_id: int, tournament_data: TournamentUpdate
) -> TournamentResponse:
    tournament = await get_tournament_by_id(db, tournament_id)
    if not tournament:
        raise ValueError("Tournament not found")

    update_dict = tournament_data.model_dump(exclude_unset=True)

    for key, value in update_dict.items():
        setattr(tournament, key, value)
    try:
        await db.commit()
        await db.refresh(tournament)
    except Exception as e:
        await db.rollback()
        raise e

    return tournament
