from app.schemas import CamelCaseModel


class PlayerCreate(CamelCaseModel):
    "Player create"

    user_id: int
    rating: int = 1000


class PlayerUpdate(CamelCaseModel):
    rating: int


class PlayerResponse(CamelCaseModel):
    id: int
    user_id: int
    rating: int
    first_name: str
    last_name: str
    email: str
