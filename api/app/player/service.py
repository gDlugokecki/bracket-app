from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.auth.service import get_user_by_id
from app.player.schemas import PlayerCreate, PlayerResponse, PlayerUpdate
from app.player.models import Player


async def get_player_by_user_id(db: AsyncSession, user_id: int) -> Optional[Player]:
    result = await db.execute(select(Player).where(Player.user_id == user_id))
    return result.scalar_one_or_none()


async def create_player(db: AsyncSession, player_data: PlayerCreate) -> PlayerResponse:
    user = await get_user_by_id(db, player_data.user_id)

    if not user:
        raise ValueError("User not found")

    existing = await get_player_by_user_id(db, player_data.user_id)

    if existing:
        raise ValueError("User already has a player profile")

    player = Player(user_id=player_data.user_id, rating=player_data.rating)

    db.add(player)

    try:
        await db.commit()
        await db.refresh(player)
    except Exception as e:
        await db.rollback()
        raise e

    return player


async def get_player_by_id(db: AsyncSession, player_id: int) -> Player:
    result = await db.execute(select(Player).options(selectinload(Player.user)).where(Player.id == player_id))
    return result.scalar_one_or_none()


async def get_all_players(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Player]:
    result = await db.execute(select(Player).options(selectinload(Player.user)).offset(skip).limit(limit))
    return list(result.scalars().all())


async def update_player(db: AsyncSession, player_id: int, player_data: PlayerUpdate) -> Player | None:
    player = await get_player_by_id(db, player_id)

    if not player:
        raise ValueError("User does not exist")

    player.rating = player_data.rating

    try:
        await db.commit()
        await db.refresh(player)
    except Exception as e:
        await db.rollback()
        raise e

    return player


async def delete_player(db: AsyncSession, player_id: int) -> bool:
    player = await get_player_by_id(db, player_id)

    if not player:
        raise ValueError("Player not found")

    await db.delete(player)

    try:
        await db.commit()
    except Exception as e:
        await db.rollback()
        raise e

    return True
