from .schemas import RefreshTokenSchema, RegisterUserInputSchema, LoginSchema
from django.contrib.auth import get_user_model, authenticate
from django.db import IntegrityError
from ninja_jwt.tokens import RefreshToken

User = get_user_model()


def create_user(data: RegisterUserInputSchema) -> tuple:
    try:
        User.objects.create_user(
            email=data.email,
            password=data.password,
            first_name=data.first_name,
            last_name=data.last_name,
        )
        return 201, {"detail": "User created"}
    except IntegrityError:
        user = User.objects.get(email=data.email)
        if user.is_active:
            return 400, {"detail", "Email already exists"}
        else:
            return 400, {"detail", "User alreadt exists but is not active"}


def login_user(request, user_data: LoginSchema) -> tuple:
    user = authenticate(request, email=user_data.email, password=user_data.password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return 200, {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    else:
        return 400, {"detail": "Invalid email or password"}


def refresh_token(data: RefreshTokenSchema) -> tuple:
    try:
        refresh = RefreshToken(data.refresh)
        return 200, {"access": str(refresh.access_token)}
    except Exception as e:
        return 400, {"detail": str(e)}


def logout(data: RefreshTokenSchema) -> tuple:
    try:
        RefreshToken(data.refresh).blacklist()
        return 200, {"detail": "Logout successful"}
    except Exception as e:
        return 400, {"detail": str(e)}
