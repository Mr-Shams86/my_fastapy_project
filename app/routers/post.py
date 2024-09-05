# app/routers/post.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database import get_db
from app.crud import create_post, get_post
from app.schemas import PostCreate, PostRead
from sqlalchemy.orm import Session
from app import crud, models, schemas


router = APIRouter()

@router.post("/posts/", response_model=PostRead)
async def create_post_view(post: PostCreate, db: AsyncSession = Depends(get_db), user_id: int = 1):
    return await create_post(db, post, user_id=user_id)

@router.get("/posts/", response_model=List[schemas.Post])
async def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@router.get("/posts/{post_id}", response_model=schemas.Post)
async def read_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

