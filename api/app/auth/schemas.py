from datetime import datetime

from pydantic import EmailStr, computed_field

from app.schemas import CamelCaseModel


class UserCreate(CamelCaseModel):
    """User create"""

    email: EmailStr
    password: str
    first_name: str
    last_name: str


class UserLogin(CamelCaseModel):
    """User login"""

    email: EmailStr
    password: str


class UserResponse(CamelCaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool
    date_joined: datetime
    player_id: int | None = None  # from relationship

    @computed_field
    @property
    def is_player(self) -> bool:
        return self.player_id is not None


class LoginResponse(CamelCaseModel):
    user: UserResponse
