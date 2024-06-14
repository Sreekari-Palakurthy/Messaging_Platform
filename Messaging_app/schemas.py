from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    userthread_id:int

class Message(MessageBase):
    id: int
    userthread_id:int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    phone_number:int

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class ThreadBase(BaseModel):
    thread_name: str

class ThreadCreate(ThreadBase):
    pass

class Thread(ThreadBase):
    id: int
    created_at:(DateTime)

    class Config:
        orm_mode = True