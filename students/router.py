from fastapi import APIRouter, HTTPException

from .schema import StudentCreateSchema, StudentUpdateSchema
from .storage import *

router = APIRouter()


@router.post("")
async def create_item(student: StudentCreateSchema):
    s = Student(
        first_name=student.first_name,
        last_name=student.last_name,
        student_id=len(STUDENTS) + 1,
    )
    STUDENTS[s.student_id] = s
    return s


@router.put("{student_id}")
async def update_item(student_id: int, student: StudentUpdateSchema):
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


@router.get("")
async def read_item():
    return STUDENTS
