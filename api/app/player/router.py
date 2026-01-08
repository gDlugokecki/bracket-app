from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.player.schemas import PlayerCreate, PlayerResponse, PlayerUpdate
from app.player.service import create_player, delete_player, get_all_players, get_player_by_id, update_player

router = APIRouter(prefix="/players", tags=["players"])


@router.get("/{player_id}", response_model=PlayerResponse)
async def get_player(player_id: int, db: AsyncSession = Depends(get_db)):
    player = await get_player_by_id(db, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.get("/", response_model=list[PlayerResponse])
async def list_players(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    players = await get_all_players(db, skip, limit)
    return players


@router.patch("/{player_id}", response_model=PlayerResponse)
async def update_player_endpoint(player_id: int, player_data: PlayerUpdate, db: AsyncSession = Depends(get_db)):
    try:
        updated_player = await update_player(db, player_id, player_data)
        return updated_player
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{player_id}", status_code=204)
async def delete_player_endpoint(player_id: int, db: AsyncSession = Depends(get_db)):
    try:
        await delete_player(db, player_id)
        return
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/", response_model=PlayerResponse, status_code=201)
async def create_player_endpoint(player_data: PlayerCreate, db: AsyncSession = Depends(get_db)):
    try:
        player = await create_player(db, player_data)
        return player
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
