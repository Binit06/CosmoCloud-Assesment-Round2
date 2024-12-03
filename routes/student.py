from fastapi import APIRouter, Body

from database.database import *
from models.student import Student
from schemas.student import UpdateStudentModel


router = APIRouter()


@router.get("/")
async def get_students():
    students = await retrieve_students()
    return {
        "data": [{"name" : student.name, "age": student.age} for student in students]
    }


@router.get("/{id}")
async def get_student_data(id: PydanticObjectId):
    student = await retrieve_student(id)
    if student:
        return {
            "name": student.name,
            "age": student.age,
            "address": {
                "city": student.address.city,
                "country": student.address.country,
            }
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Student doesn't exist",
    }


@router.post("/")
async def add_student_data(student: Student = Body(...)):
    new_student = await add_student(student)
    return {
        "id" : new_student.id.__str__()
    }


@router.delete("/{id}")
async def delete_student_data(id: PydanticObjectId):
    deleted_student = await delete_student(id)
    if deleted_student:
        return {}
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Student with id {0} doesn't exist".format(id),
        "data": False,
    }


@router.patch("/{id}")
async def update_student(id: PydanticObjectId, req: UpdateStudentModel = Body(...)):
    updated_student = await update_student_data(id, req.dict())
    if updated_student:
        return {}
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Student with ID: {} not found".format(id),
        "data": False,
    }