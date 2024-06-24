from sqlalchemy.orm import Session
from thread import models, schemas

def create_thread(db: Session, thread: schemas.ThreadBase):
    db_thread = models.Thread(**thread.dict())
    db.add(db_thread)
    db.commit()
    db.refresh(db_thread)
    return db_thread

def get_thread(db: Session, thread_id: int):
    return db.query(models.Thread).filter(models.Thread.id == thread_id).first()