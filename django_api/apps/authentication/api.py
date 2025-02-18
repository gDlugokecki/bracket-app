from ninja import Router
from ninja.responses import codes_2xx
from .commands import create_user, login_user

from .schemas import (
    RegisterUserInputSchema,
    SuccessResponse,
    ErrorResponse,
    LoginSchema,
    TokenPairSchema,
)

auth_router = Router(tags=["auth"])


@auth_router.post(
    "/login",
    response={codes_2xx: TokenPairSchema, 400: ErrorResponse},
)
def login(request, data: LoginSchema):
    status_code, response_data = login_user(request, data)
    return status_code, response_data


@auth_router.post(
    "/register",
    response={codes_2xx: SuccessResponse, 400: ErrorResponse},
)
def register(request, data: RegisterUserInputSchema):
    status_code, response_data = create_user(data)
    return status_code, response_data
