from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    phone_number:int

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class ThreadBase(BaseModel):
    title: str

class Thread(ThreadBase):
    id: int

    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    sender_id: int
    receiver_id: int
    thread_id: int

class Message(MessageBase):
    id: int
    sender_id: int
    receiver_id: int
    thread_id: int

    class Config:
        orm_mode = True