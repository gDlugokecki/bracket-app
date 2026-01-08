from pydantic import BaseModel, ConfigDict


class PlayerCreate(BaseModel):
    "Player create"

    user_id: int
    rating: int = 1000


class PlayerUpdate(BaseModel):
    rating: int


class PlayerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    rating: int
    first_name: str
    last_name: str
    email: str
