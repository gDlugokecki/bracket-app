from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from starlette.middleware.sessions import SessionMiddleware

from app.admin import AdminAuth, MatchAdmin, PlayerAdmin, TeamAdmin, TournamentAdmin, UserAdmin
from app.auth.router import router as auth_router
from app.config import settings
from app.database import engine
from app.match.router import router as match_router
from app.player.router import router as player_router
from app.tournament.router import router as tournament_router

app = FastAPI(title="Bracket App API", version="1.0.0")
app.add_middleware(SessionMiddleware, secret_key=settings.secret_key)

authentication_backend = AdminAuth(secret_key=settings.secret_key)
admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)
admin.add_view(PlayerAdmin)
admin.add_view(TournamentAdmin)
admin.add_view(TeamAdmin)
admin.add_view(MatchAdmin)


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(player_router)
app.include_router(tournament_router)
app.include_router(match_router)
