from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    phone_number: int

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True