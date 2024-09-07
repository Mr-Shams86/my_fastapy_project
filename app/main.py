from fastapi import FastAPI, Request, HTTPException
from jose import JWTError, jwt
from app.config import settings
from app.middleware import JWTMiddleware
from fastapi import FastAPI
from app.routers import post, user

app = FastAPI()


# Подключение маршрутов
app.include_router(post.router, prefix="/posts", tags=["posts"])
app.include_router(user.router, prefix="/users", tags=["users"])

app.add_middleware(JWTMiddleware)

