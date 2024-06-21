from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, databases
from typing import List


app = FastAPI()

def get_db():
    db = databases.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=models.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = user.hashed_password  # You should implement a secure password hashing function
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}/", response_model=models.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await db.get(models.User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# API endpoints for threads
@app.post("/threads/", response_model=models.Thread)
async def create_thread(thread: models.Thread, db: Session = Depends(get_db)):
    db_thread = models.Thread(**thread.dict())
    db.add(db_thread)
    await db.commit()
    await db.refresh(db_thread)
    return db_thread

@app.get("/threads/{thread_id}/", response_model=schemas.ThreadInDB)
async def read_thread(thread_id: int, db: Session = Depends(get_db)):
    db_thread = await db.get(models.Thread, thread_id)
    if db_thread is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return db_thread

# API endpoints for messages
@app.post("/messages/", response_model=models.Message)
async def create_message(message: schemas.MessageBase, db: Session = Depends(get_db)):
    db_message = models.Message(**message.dict(), created_at=datetime.utcnow())
    db.add(db_message)
    await db.commit()
    await db.refresh(db_message)
    return db_message

@app.get("/messages/{message_id}/", response_model=models.Message)
async def read_message(message_id: int, db: Session = Depends(get_db)):
    db_message = await db.get(models.Message, message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

# New endpoint to retrieve all messages by a specific user
@app.post("/users/{user_id}/messages/", response_model=List[models.Message])
async def get_user_messages(user_id: int, db: Session = Depends(get_db)):
    messages = await db.query(models.Message).filter(models.Message.sender_id == user_id).all()
    return messages
