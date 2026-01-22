from datetime import datetime

from pydantic import EmailStr

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


class LoginResponse(CamelCaseModel):
    user: UserResponse
