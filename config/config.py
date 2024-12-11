from typing import Optional
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings
from models import Movie, Comment, User, Theater  # Import the models explicitly

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    secret_key: str = "secret"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev"
        from_attributes = True

async def initiate_database():
    settings = Settings()
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    database = client["sample_mflix"]

    try:
        await init_beanie(
            database=database,
            document_models=[Movie]
        )
        print("Movie model initialized successfully!")
    except Exception as e:
        print(f"Error initializing Movie model: {e}")