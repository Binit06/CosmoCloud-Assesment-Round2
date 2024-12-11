from pydantic import BaseModel, Field
from datetime import datetime
from beanie import Document

class Comment(Document):
    name: str
    email: str
    text: str
    date: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "text": "This movie was amazing!",
                "date": "2024-08-09T12:34:56.789Z"
            }
        }

    class Settings:
        name = "comments"
