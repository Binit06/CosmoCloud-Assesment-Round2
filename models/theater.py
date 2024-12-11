from beanie import Document
from pydantic import BaseModel

class Location(BaseModel):
    address: str
    city: str
    state: str
    postal_code: str

    class Config:
        json_schema_extra = {
            "example": {
                "address": "123 Main Street",
                "city": "Los Angeles",
                "state": "CA",
                "postal_code": "90001"
            }
        }

class Theater(Document):
    location: Location

    class Config:
        json_schema_extra = {
            "example": {
                "location": {
                    "address": "123 Main Street",
                    "city": "Los Angeles",
                    "state": "CA",
                    "postal_code": "90001"
                }
            }
        }

    class Settings:
        name = "theaters"
