from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.hashed_password
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password, phone_number=user.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_thread(db: Session, thread: schemas.ThreadBase):
    db_thread = models.Thread(**thread.dict())
    db.add(db_thread)
    db.commit()
    db.refresh(db_thread)
    return db_thread

def get_thread(db: Session, thread_id: int):
    return db.query(models.Thread).filter(models.Thread.id == thread_id).first()

def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Message).offset(skip).limit(limit).all()