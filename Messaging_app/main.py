from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud,schemas, databases,models
from databases import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = databases.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/threads/", response_model=schemas.Thread)
def create_thread(thread: schemas.ThreadBase, db: Session = Depends(get_db)):
    return crud.create_thread(db=db, thread=thread)

@app.get("/threads/{thread_id}", response_model=schemas.Thread)
def read_thread(thread_id: int, db: Session = Depends(get_db)):
    db_thread = crud.get_thread(db, thread_id=thread_id)
    if db_thread is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return db_thread

@app.post("/messages/", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.get("/messages/", response_model=list[schemas.Message])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = crud.get_messages(db, skip=skip, limit=limit)
    return messages

@app.get("/users/{user_id}/messages", response_model=list[schemas.Message])
def read_user_messages(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    messages = crud.get_user_messages(db, user_id=user_id)
    return messages