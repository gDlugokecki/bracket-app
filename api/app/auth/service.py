from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.schemas import UserCreate
from app.auth.security import hash_password, verify_password
from app.auth.models import RefreshToken, User


async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    hashed_password = hash_password(user_data.password)

    user = User(
        email=user_data.email, password=hashed_password, first_name=user_data.first_name, last_name=user_data.last_name
    )

    db.add(user)

    try:
        await db.commit()
        await db.refresh(user)
    except Exception as e:
        await db.rollback()
        raise e

    return user


async def authenticate_user(db: AsyncSession, email: str, password: str) -> Optional[User]:
    user = await get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    if not user.is_active:
        return None

    return user


async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def create_refresh_token_db(db: AsyncSession, token: str, user_id: int, expires_at: datetime) -> RefreshToken:
    db_token = RefreshToken(token=token, user_id=user_id, expires_at=expires_at)
    db.add(db_token)
    await db.commit()
    await db.refresh(db_token)
    return db_token


async def get_valid_refresh_token(db: AsyncSession, token: str) -> Optional[RefreshToken]:
    result = await db.execute(
        select(RefreshToken).where(
            RefreshToken.token == token,
            ~RefreshToken.is_revoked,
            RefreshToken.expires_at > datetime.now(timezone.utc),
        )
    )
    return result.scalar_one_or_none()


async def revoke_refresh_token(db: AsyncSession, token: str):
    result = await db.execute(select(RefreshToken).where(RefreshToken.token == token))
    db_token = result.scalar_one_or_none()

    if db_token:
        db_token.is_revoked = True
        await db.commit()
