from pydantic import BaseModel

class ThreadBase(BaseModel):
    title: str
    owner_id: int

class Thread(ThreadBase):
    id: int

    class Config:
        orm_mode = True
