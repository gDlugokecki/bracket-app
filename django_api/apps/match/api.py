from core.utility.MyRouter import MyRouter as Router

match_router = Router(tags=["match"])


@match_router.get("/")
def get_match(request):
    return "Hello match"
