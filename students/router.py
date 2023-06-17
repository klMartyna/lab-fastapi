from fastapi import APIRouter, HTTPException

from .schema import StudentCreateSchema, StudentUpdateSchema
from .storage import *

router = APIRouter()


@router.get("")
async def read_all_students():
    return STUDENTS


@router.get("/{student_id}")
async def read_student(student_id: int):
    if student_id not in STUDENTS.keys():
        raise HTTPException(status_code=404, detail="Student not found")
    
    return {f"{student_id}": STUDENTS[student_id]}


@router.post("")
async def create_student(student: StudentCreateSchema):
    if student.first_name == "" or student.last_name == "":
        raise HTTPException(status_code=422, detail="Empty student data")
    
    if len(STUDENTS) == 0:
        id = 1
    else:
        id = list(STUDENTS)[-1] + 1

    new_student = Student(
    **student.dict(),
    student_id=id,
    )
    STUDENTS[id] = new_student
    MARKS[id] = []

    return new_student


@router.delete("/{student_id}")
async def delete_student(student_id: int):
    if student_id not in STUDENTS.keys():
        raise HTTPException(status_code=404, detail="Student not found")
    
    del STUDENTS[student_id]
    del MARKS[student_id]

    return {"Student deleted": True}


@router.put("/{student_id}")
async def update_student(student_id: int, student: StudentUpdateSchema):
    if student_id not in STUDENTS.keys():
        raise HTTPException(status_code=404, detail="Student not found")
    if student.first_name == "" or student.last_name == "":
        raise HTTPException(status_code=422, detail="Empty student data")
    
    updated_student = Student(
        first_name=student.first_name,
        last_name=student.last_name,
        student_id=student_id,
    )
    STUDENTS[updated_student.student_id] = updated_student

    return updated_student

@router.post("/{student_id}/marks/{mark:float}")
async def create_mark(student_id: int, mark: Mark):
    if student_id not in STUDENTS.keys():
        raise HTTPException(status_code=404, detail="Student not found")

    new_mark = Mark(mark)
    MARKS[student_id].append(new_mark)

    return new_mark

@router.get("/{student_id}/marks")
async def read_marks(student_id: int):
    if student_id not in STUDENTS.keys():
        raise HTTPException(status_code=404, detail="Student not found")
    
    return MARKS[student_id]