from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    timestamp: datetime
    thread_id: int
    user_id: int

    class Config:
        orm_mode = True

class ThreadBase(BaseModel):
    title: str

class ThreadCreate(ThreadBase):
    pass

class Thread(ThreadBase):
    id: int
    owner_id: int
    messages: List[Message] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    phone_no:int

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    threads: List[Thread] = []

    class Config:
        orm_mode = True
