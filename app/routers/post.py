from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database import get_db
from app.crud import create_post, get_post, get_posts
from app.schemas import PostCreate, Post, User
from app.services.security import get_current_user

router = APIRouter()

@router.post("/posts/", response_model=Post)
async def create_post_view(post: PostCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await create_post(db, post, user_id=current_user.id)

@router.get("/posts/", response_model=List[Post])
async def read_posts(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_posts(db, skip=skip, limit=limit)

@router.get("/posts/{post_id}", response_model=Post)
async def read_post(post_id: int, db: AsyncSession = Depends(get_db)):
    db_post = await get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post





