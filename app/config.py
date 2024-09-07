import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://fastapi_user:fastapi_password@db:5432/fastapi_db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    MEDIA_DIR_NAME: str = os.getenv("MEDIA_DIR_NAME", "media")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "local")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "debug")
    CURRENT_DOMAIN: str = os.getenv("CURRENT_DOMAIN", "http://127.0.0.1:8000")

settings = Settings()



