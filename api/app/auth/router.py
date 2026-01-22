from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Cookie, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.security import create_refresh_token, decode_access_token
from app.auth.models import User
from app.database import get_db
from app.auth.security import create_access_token
from app.auth.service import (
    authenticate_user,
    create_refresh_token_db,
    create_user,
    get_user_by_email,
    get_user_by_id,
    get_valid_refresh_token,
    revoke_refresh_token,
)
from app.auth.schemas import LoginResponse, UserCreate, UserLogin, UserResponse


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter(prefix="/auth", tags=["auth"])


async def get_current_user(access_token: str = Cookie(None), db: AsyncSession = Depends(get_db)) -> User:
    if not access_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    payload = decode_access_token(access_token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

    email: str = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

    user = await get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive user")

    return user


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED, operation_id="register")
async def register(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    user = await create_user(db, user_data)

    return user


@router.post("/login", response_model=LoginResponse, operation_id="login")
async def login(login_data: UserLogin, response: Response, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, email=login_data.email, password=login_data.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": user.email})
    refresh_token_str = create_refresh_token(data={"sub": str(user.id)})
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)

    await create_refresh_token_db(db, token=refresh_token_str, user_id=user.id, expires_at=expires_at)

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  # TODO: CHANGE IN PRODUCTION
        samesite="lax",
        max_age=1800,
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token_str,
        httponly=True,
        secure=False,  # TODO: CHANGE IN PRODUCTION
        samesite="lax",
        max_age=604800,  # 7 days,
    )

    return {"user": user}


@router.get("/me", response_model=UserResponse, operation_id="getMe")
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/logout", operation_id="logout")
async def logout(response: Response, refresh_token: str = Cookie(None), db: AsyncSession = Depends(get_db)):
    if refresh_token:
        await revoke_refresh_token(db, refresh_token)

    response.delete_cookie(key="access_token", path="/", samesite="lax")
    response.delete_cookie(key="refresh_token", path="/", samesite="lax")
    return {"message": "Logout successful"}


@router.post("/refresh", operation_id="refresh-token")
async def refresh_token(response: Response, refresh_token: str = Cookie(None), db: AsyncSession = Depends(get_db)):
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Refresh token missing")

    db_token = await get_valid_refresh_token(db, refresh_token)
    if not db_token:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    user = await get_user_by_id(db, db_token.user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found or inactive")

    new_access_token = create_access_token(data={"sub": user.email})
    new_refresh_token_str = create_refresh_token(data={"sub": str(user.id)})

    await revoke_refresh_token(db, refresh_token)
    await create_refresh_token_db(
        db, new_refresh_token_str, user.id, expires_at=datetime.now(timezone.utc) + timedelta(days=7)
    )

    response.set_cookie(
        key="access_token",
        value=new_access_token,
        httponly=True,
        secure=False,  # TODO: CHANGE IN PRODUCTION
        samesite="lax",
        max_age=1800,
    )

    response.set_cookie(
        key="refresh_token",
        value=new_refresh_token_str,
        httponly=True,
        secure=False,  # TODO: CHANGE IN PRODUCTION
        samesite="lax",
        max_age=604800,  # 7 days
    )

    return {"message": "Token refreshed"}
