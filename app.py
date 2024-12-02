from fastapi import FastAPI, Depends
from fastapi.concurrency import asynccontextmanager

from config.config import initiate_database
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from routes.student import router as StudentRouter

async def start_database():
    await initiate_database()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_database()
    scheduler = AsyncIOScheduler(timezone="UTC")
    scheduler.add_job(func=start_database, trigger="interval", seconds=300)
    scheduler.start()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this app. This is speceifically made for intern assessment purpose."} 

app.include_router(StudentRouter,tags=["Students"],prefix="/students")