"""SQLAdmin configuration for Bracket App models"""

from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.auth.models import User
from app.auth.security import verify_password
from app.database import async_session_maker
from app.match.models import Match
from app.player.models import Player
from app.team.models import Team
from app.tournament.models import Tournament


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email = form.get("username")
        password = form.get("password")

        if not email or not password:
            return False

        async with async_session_maker() as session:
            from sqlalchemy import select

            result = await session.execute(select(User).where(User.email == email))
            user = result.scalar_one_or_none()

            if not user:
                return False

            if not verify_password(password, user.password):
                return False

            if not user.is_active or not user.is_superuser:
                return False

            request.session.update({"user_id": user.id})
            return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> RedirectResponse | bool:
        user_id = request.session.get("user_id")

        if not user_id:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        async with async_session_maker() as session:
            from sqlalchemy import select

            result = await session.execute(select(User).where(User.id == user_id))
            user = result.scalar_one_or_none()

            if not user or not user.is_active or not user.is_superuser:
                return RedirectResponse(request.url_for("admin:login"), status_code=302)

        return True


class UserAdmin(ModelView, model=User):
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"

    column_list = [User.id, User.email, User.first_name, User.last_name, User.is_active, User.is_superuser, User.date_joined]
    column_searchable_list = [User.email, User.first_name, User.last_name]
    column_sortable_list = [User.id, User.email, User.date_joined]
    column_default_sort = [(User.date_joined, True)]

    form_columns = [User.email, User.first_name, User.last_name, User.is_active, User.is_superuser]

    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True


class PlayerAdmin(ModelView, model=Player):
    name = "Player"
    name_plural = "Players"
    icon = "fa-solid fa-user-check"

    column_list = [Player.id, Player.user_id, Player.rating]
    column_searchable_list = []
    column_sortable_list = [Player.id, Player.rating]
    column_default_sort = [(Player.rating, True)]

    form_columns = [Player.user_id, Player.rating]

    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True


class TournamentAdmin(ModelView, model=Tournament):
    name = "Tournament"
    name_plural = "Tournaments"
    icon = "fa-solid fa-trophy"

    column_list = [
        Tournament.id,
        Tournament.name,
        Tournament.start_date,
        Tournament.end_date,
        Tournament.location,
        Tournament.category,
    ]
    column_searchable_list = [Tournament.name, Tournament.location, Tournament.category]
    column_sortable_list = [Tournament.id, Tournament.name, Tournament.start_date]
    column_default_sort = [(Tournament.start_date, True)]

    form_columns = [
        Tournament.name,
        Tournament.start_date,
        Tournament.end_date,
        Tournament.location,
        Tournament.category,
        Tournament.players,
    ]

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class TeamAdmin(ModelView, model=Team):
    name = "Team"
    name_plural = "Teams"
    icon = "fa-solid fa-people-group"

    column_list = [Team.id, Team.name]
    column_searchable_list = [Team.name]
    column_sortable_list = [Team.id]

    form_columns = [Team.name, Team.players]

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class MatchAdmin(ModelView, model=Match):
    name = "Match"
    name_plural = "Matches"
    icon = "fa-solid fa-table-tennis-paddle-ball"

    column_list = [
        Match.id,
        Match.tournament_id,
        Match.team1_id,
        Match.team2_id,
        Match.status,
        Match.scheduled_time,
        Match.court_number,
        Match.round_number,
        Match.score,
        Match.winner_team_id,
    ]
    column_searchable_list = [Match.court_number]
    column_sortable_list = [Match.id, Match.scheduled_time, Match.status, Match.round_number]
    column_default_sort = [(Match.scheduled_time, False)]

    form_columns = [
        Match.tournament,
        Match.team1,
        Match.team2,
        Match.status,
        Match.scheduled_time,
        Match.court_number,
        Match.round_number,
        Match.score,
        Match.duration,
        Match.winner_team,
    ]

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
