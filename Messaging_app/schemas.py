from pydantic import BaseModel
from models import DateTime 
from typing import List


class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class ThreadBase(BaseModel):
    title: str

class Thread(ThreadBase):
    creator_id: int

class ThreadInDB(Thread):
    id: int
    creator: User
    messages: List["Message"]

    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    content: str
    sender_id: int
    thread_id: int

class Message(MessageBase):
    id: int
    created_at: DateTime
    sender: User
    thread_id: int

    class Config:
        orm_mode = True