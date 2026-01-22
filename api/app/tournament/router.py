from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.tournament.schemas import TournamentCreate, TournamentResponse, TournamentUpdate
from app.tournament.service import (
    add_player_to_tournament,
    create_tournament,
    delete_tournament,
    get_all_tournaments,
    get_tournament_by_id,
    remove_player_from_tournament,
    update_tournament,
)


router = APIRouter(prefix="/tournaments", tags=["tournaments"])


@router.get("/{tournament_id}", response_model=TournamentResponse, operation_id="getTournament")
async def get_tournament_by_id_endpoint(tournament_id: int, db: AsyncSession = Depends(get_db)):
    tournament = await get_tournament_by_id(db, tournament_id)

    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament does not exists")
    return tournament


@router.get("/", response_model=list[TournamentResponse], operation_id="listTournaments")
async def list_tournaments(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    tournaments = await get_all_tournaments(db, skip, limit)
    return tournaments


@router.post("/", response_model=TournamentResponse, status_code=201, operation_id="createTournament")
async def create_tournament_endpoint(tournament_data: TournamentCreate, db: AsyncSession = Depends(get_db)):
    try:
        tournament = await create_tournament(db, tournament_data)
        return tournament
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{tournament_id}", status_code=204, operation_id="deleteTournament")
async def delete_tournament_endpoint(tournament_id: int, db: AsyncSession = Depends(get_db)):
    try:
        await delete_tournament(db, tournament_id)
        return
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{tournament_id}/players/{player_id}", status_code=204, operation_id="removePlayerFromTournament")
async def remove_player_from_tournament_endpoint(
    tournament_id: int, player_id: int, db: AsyncSession = Depends(get_db)
):
    try:
        await remove_player_from_tournament(db, tournament_id, player_id)
        return
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{tournament_id}/players/{player_id}", response_model=TournamentResponse, status_code=201, operation_id="addPlayerToTournament")
async def add_player_to_tournament_endpoint(tournament_id: int, player_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await add_player_to_tournament(db, tournament_id, player_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{tournament_id}", response_model=TournamentResponse, operation_id="updateTournament")
async def update_tournament_endpoint(
    tournament_id: int, tournament_data: TournamentUpdate, db: AsyncSession = Depends(get_db)
):
    try:
        updated_tournament = await update_tournament(db, tournament_id, tournament_data)
        return updated_tournament
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
