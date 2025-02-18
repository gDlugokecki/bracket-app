from ninja import Router
from typing import List
from .schemas import TournamentListSchema, TournamentSchema
from .models import Tournament
from apps.match.models import Match
from apps.match.schemas import MatchSchema
from django.shortcuts import get_object_or_404

tournament_router = Router(tags=["tournament"])


@tournament_router.get("/", response=List[TournamentListSchema])
def list_tournaments(request):
    return Tournament.objects.all()


@tournament_router.get("/{tournament_id}", response=TournamentSchema)
def get_tournament(request, tournament_id: int):
    return get_object_or_404(Tournament, id=tournament_id)


@tournament_router.get("/{tournament_id}/matches", response=List[MatchSchema])
def get_tournament_matches(request, tournament_id: int):
    matches = Match.objects.filter(tournament_id=tournament_id)
    return matches
