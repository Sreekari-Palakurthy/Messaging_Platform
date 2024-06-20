from databases import SessionLocal,engine
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(username=user.username, email=user.email,phone_no=user.phone_no)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@app.post("/threads/", response_model=schemas.Thread)
def create_thread(thread: schemas.ThreadCreate, db: Session = Depends(get_db), user_id=int):
    db_thread = models.Thread(**thread.dict(), owner_id=user_id)
    db.add(db_thread)
    db.commit()
    db.refresh(db_thread)
    return db_thread

@app.get("/threads/", response_model=List[schemas.Thread])
def read_threads(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    threads = db.query(models.Thread).offset(skip).limit(limit).all()
    return threads

@app.post("/messages/", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db), thread_id=int, user_id=int):
    db_message = models.Message(**message.dict(), thread_id=thread_id, user_id=user_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.get("/messages/", response_model=List[schemas.Message])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = db.query(models.Message).offset(skip).limit(limit).all()
    return messages
