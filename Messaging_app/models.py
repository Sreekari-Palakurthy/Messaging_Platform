from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from databases import Base, SessionLocal, engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    threads = relationship("Thread", back_populates="creator")
    messages = relationship("Message", back_populates="sender")

class Thread(Base):
    __tablename__ = 'threads'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    creator_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="threads")
    messages = relationship("Message", back_populates="thread")

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    sender_id = Column(Integer, ForeignKey('users.id'))
    thread_id = Column(Integer, ForeignKey('threads.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    sender = relationship("User", back_populates="messages")
    thread = relationship("Thread", back_populates="messages")



Base.metadata.create_all(bind=engine)
