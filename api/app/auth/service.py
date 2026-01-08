from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.schemas import UserCreate
from app.auth.security import hash_password, verify_password
from app.auth.models import User


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
