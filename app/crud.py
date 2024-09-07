from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas
from app.models import Post, User
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

# Настройка контекста для хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Функция для хеширования пароля
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

async def create_post(db: AsyncSession, post: schemas.PostCreate, user_id: int):
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

async def get_user_by_email(db: AsyncSession, email: str) -> User:
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user_create: schemas.UserCreate):
    # Проверка на существующий email
    existing_user = await get_user_by_email(db, user_create.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Хеширование пароля
    hashed_password = get_password_hash(user_create.password)
    
    # Создание нового пользователя
    new_user = User(username=user_create.username, email=user_create.email, hashed_password=hashed_password)
    db.add(new_user)
    
    try:
        await db.commit()
        await db.refresh(new_user)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Error creating user")
    
    return new_user






