from sqlalchemy.orm import Session
from user import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.hashed_password
    db_user = models.User(username=user.username, email=user.email, hashed_password=user.hashed_password, phone_number=user.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()