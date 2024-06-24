from pydantic import BaseModel


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
