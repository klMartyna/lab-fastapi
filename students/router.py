from fastapi import APIRouter, HTTPException

from .schema import StudentCreateSchema, StudentUpdateSchema
from .storage import *

router = APIRouter()


@router.get("")
async def read_all_students():
    return STUDENTS


@router.get("/{student_id}")
async def read_student(student_id: int):
    return {f"{student_id}": STUDENTS[student_id]}


@router.post("")
async def create_student(student: StudentCreateSchema):
    id = len(STUDENTS) + 1
    new_student = Student(
        **student.dict(),
        student_id=id,
    )
    if new_student.first_name == "" or new_student.last_name == "":
        raise HTTPException(status_code=400, detail="Empty student data")
    else:
        STUDENTS[id] = new_student

    return new_student


@router.delete("/{student_id}")
async def delete_student(student_id: int):
    if student_id not in STUDENTS.keys():
        raise HTTPException(status_code=404, detail="Student not found")
    else:
        del STUDENTS[student_id]

    return {"Student deleted": True}


@router.put("/{student_id}")
async def update_student(student_id: int, student: StudentUpdateSchema):
    if student_id not in STUDENTS.keys():
        raise HTTPException(status_code=404, detail="Student not found")
    else:
        updated_student = Student(
            first_name=student.first_name,
            last_name=student.last_name,
            student_id=student_id,
        )
        STUDENTS[updated_student.student_id] = updated_student

    return updated_student
