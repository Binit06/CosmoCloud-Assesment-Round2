from pydantic import BaseModel
from beanie import Document
class Address(BaseModel):
    city: str
    country: str

    class Config:
        json_schema_extra = {
            "example": {
                "city": "New York",
                "country": "USA"
            }
        }

class Student(Document):
    name: str
    age: int
    address: Address

    class Config:
        json_schema_extra = {
            "example": {
                "name" : "Binit Lenka",
                "age" : 20,
                "address": {
                    "city" : "New York",
                    "country" : "USA",
                }
            }
        }
    
    class Settings:
        name = "students"