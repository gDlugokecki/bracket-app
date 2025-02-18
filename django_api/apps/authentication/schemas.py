from ninja import Schema
from pydantic import EmailStr


class LoginSchema(Schema):
    email: EmailStr
    password: str


class RegisterUserInputSchema(LoginSchema):
    first_name: str
    last_name: str


class SuccessResponse(Schema):
    detail: str


class ErrorResponse(Schema):
    detail: str | dict | list[str]


class RefreshTokenSchema(Schema):
    refresh: str


class AccessTokenSchema(Schema):
    access: str


class TokenPairSchema(RefreshTokenSchema, AccessTokenSchema):
    pass
