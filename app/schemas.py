from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

from pydantic.types import conint



class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode=True





class PostBase(BaseModel):
    title: str = "resposta padrao"
    content: str = "teste content"
    published: bool = True

    class Config:
        orm_mode=True

class PostCreate(PostBase):
    pass


class Post(PostBase):
    created_at: datetime
    id: int
    owner_id: int
    owner: UserOut


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    acess_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)



class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode=True