from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email=Column(String, unique=True)
    phone_number=Column(Integer,unique=True)
    password = Column(String)

class Thread(Base):
    __tablename__="threads"
    id=Column(Integer,primary_key=True,index=True)
    thread_name=Column(String,unique=True)

class Message(Base):
    __tablename__="messages"
    messages_id=Column(Integer,primary_key=True,index=True)
    content=Column(String, nullable=False)
    users_id=Column(Integer,foreign_key=True)

    
