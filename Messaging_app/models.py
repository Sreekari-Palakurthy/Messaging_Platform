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
    phone_number = Column(Integer,unique=True)
    threads = relationship("Thread", back_populates="owner")
    messages_sent = relationship("Message", foreign_keys="[Message.sender_id]", back_populates="sender")
    messages_received = relationship("Message", foreign_keys="[Message.receiver_id]", back_populates="receiver")
    
class Thread(Base):
    __tablename__ = 'threads'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="threads")
    messages = relationship("Message", back_populates="thread")

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    thread_id = Column(Integer, ForeignKey('threads.id'))
    content = Column(String, index=True)
    sender = relationship("User", foreign_keys=[sender_id], back_populates="messages_sent")
    receiver = relationship("User", foreign_keys=[receiver_id], back_populates="messages_received")
    thread = relationship("Thread", back_populates="messages")

Base.metadata.create_all(bind=engine)
