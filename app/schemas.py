# These classes define Pydantic models for representing posts and users with different fields for
# creation and reading purposes.
# app/schemas.py

from pydantic import BaseModel

class UserCreate(BaseModel):
    login: str
    password: str  # Обычный пароль, который будет зашифрован перед сохранением
    name: str = None

class UserLogin(BaseModel):
    login: str
    password: str  # Пароль для входа

class UserOut(BaseModel):
    id: int
    login: str
    name: str

    class Config:
        orm_mode = True


