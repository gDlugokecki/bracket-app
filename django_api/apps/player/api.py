from ninja import Router


player_router = Router(tags=["player"])


@player_router.get("/")
def get_player(request):
    return "Hello player"
