from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.match.schemas import MatchCreate, MatchResponse, MatchUpdate
from app.match.service import create_match, delete_match, get_all_matches, get_match_by_id, update_match


router = APIRouter(prefix="/matches", tags=["matches"])


@router.get("/{match_id}", response_model=MatchResponse)
async def get_match(match_id: int, db: AsyncSession = Depends(get_db)):
    match = await get_match_by_id(db, match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match


@router.get("/", response_model=list[MatchResponse])
async def get_match_list(
    tournament_id: int | None = None, skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    matches = await get_all_matches(db, tournament_id, skip, limit)
    return matches


@router.post("/", response_model=MatchResponse, status_code=201)
async def create_match_endpoint(match_data: MatchCreate, db: AsyncSession = Depends(get_db)):
    try:
        match = await create_match(db, match_data)
        return match
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{match_id}", status_code=204)
async def delete_match_endpoint(match_id: int, db: AsyncSession = Depends(get_db)):
    try:
        await delete_match(db, match_id)
        return
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{match_id}", response_model=MatchResponse)
async def update_match_endpoint(match_id: int, match_data: MatchUpdate, db: AsyncSession = Depends(get_db)):
    try:
        updated_match = await update_match(db, match_id, match_data)
        return updated_match
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
