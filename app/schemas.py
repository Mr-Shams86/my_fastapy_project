from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    image_url:str

    class Config:
        from_attributes = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


