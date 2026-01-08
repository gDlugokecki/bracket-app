from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    """User create"""

    email: EmailStr
    password: str
    first_name: str
    last_name: str


class UserLogin(BaseModel):
    """User login"""

    email: EmailStr
    password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool
    date_joined: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
