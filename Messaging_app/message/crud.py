from sqlalchemy.orm import Session
from message import models,schemas


def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Message).offset(skip).limit(limit).all()

def get_user_messages(db: Session, user_id: int):
    return db.query(models.Message).filter(models.Message.sender_id == user_id).all()