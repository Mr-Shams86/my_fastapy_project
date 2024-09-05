# app/main.py
import asyncio
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import user, post
from app.middleware import JWTMiddleware

app = FastAPI()


app.add_middleware(JWTMiddleware)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await create_tables()

app.include_router(user.router)
app.include_router(post.router)

