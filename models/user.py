from beanie import Document
from pydantic import BaseModel, Field
from typing import List, Optional

class User(Document):
    name: str
    email: str
    password: str
    favorite_genres: Optional[List[str]] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Alice",
                "email": "alice@example.com",
                "password": "securepassword123",
                "favorite_genres": ["Drama", "Romance"]
            }
        }

    class Settings:
        name = "users"
