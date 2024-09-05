# app/crud.py

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, Post
from app.schemas import UserCreate, PostCreate

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(username=user.username, hashed_password=user.password, name=user.name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user(db: AsyncSession, username: str):
    result = await db.execute(select(User).filter(User.username == username))
    return result.scalars().first()

async def create_post(db: AsyncSession, post: PostCreate, user_id: int):
    db_post = Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post

async def get_post(db: AsyncSession, post_id: int):
    result = await db.execute(select(Post).filter(Post.id == post_id))
    return result.scalars().first()

async def get_posts(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Post).offset(skip).limit(limit))
    return result.scalars().all()

