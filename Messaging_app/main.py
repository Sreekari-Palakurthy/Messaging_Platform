from fastapi import FastAPI, Depends, HTTPException
from databases import SessionLocal, engine
from sqlalchemy.ext.declarative import declarative_base
from databases import Base, engine
from user.views import router as user_router
from thread.views import router as thread_router
from message.views import router as message_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(thread_router, prefix="/threads", tags=["threads"])
app.include_router(message_router, prefix="/messages", tags=["messages"])