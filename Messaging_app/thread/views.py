from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from databases import SessionLocal
from thread import schemas, crud

router=APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/threads/", response_model=schemas.Thread)
def create_thread(thread: schemas.ThreadBase, db: Session = Depends(get_db)):
    return crud.create_thread(db=db, thread=thread)

@router.get("/threads/{thread_id}", response_model=schemas.Thread)
def read_thread(thread_id: int, db: Session = Depends(get_db)):
    db_thread = crud.get_thread(db, thread_id=thread_id)
    if db_thread is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return db_thread