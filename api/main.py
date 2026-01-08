from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.player.router import router as player_router
from app.tournament.router import router as tournament_router
from app.match.router import router as match_router


app = FastAPI(title="Bracket App API", version="1.0.0")


app.include_router(auth_router)
app.include_router(player_router)
app.include_router(tournament_router)
app.include_router(match_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
