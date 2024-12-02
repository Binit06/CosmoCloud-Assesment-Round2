from pydantic import BaseModel
from typing import Optional, Any

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

class Student(BaseModel):
    name: str
    age: int
    address: Address

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 25,
                "address": {
                    "city": "New York",
                    "country": "USA"
                }
            }
        }

class UpdateStudentModel(BaseModel):
    name: str
    age: int
    address: Address

    class Collection:
        name = "students"

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 25,
                "address": {
                    "city": "New York",
                    "country": "USA"
                }
            }
        }

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "status_code" : 200,
                "response_type" : "success",
                "description" : "Student data retrieved successfully",
                "data": "Sample Data"
            }
        }