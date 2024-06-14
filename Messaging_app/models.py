from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
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
    created_at=Column(DateTime)

class UserThread(Base):
    __tablename__="userthread"
    id=Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("users.id"), nullable=False)
    thread_id=Column(Integer,ForeignKey("threads.id"),nullable=False)

class Message(Base):
    __tablename__="messages"
    id=Column(Integer,primary_key=True,index=True)
    content=Column(String, nullable=False)
    sent_at=Column(DateTime)
    userthread_id=Column(Integer, ForeignKey("userthread.id"),nullable=False)
    

    
