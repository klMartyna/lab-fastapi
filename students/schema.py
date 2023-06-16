from pydantic import BaseModel
from enum import Enum


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Jerzetta",
                "last_name": "Kłosińska",
            }
        }


class StudentUpdateSchema(BaseModel):
    first_name: str
    last_name: str


class Student(BaseModel):
    student_id: int
    first_name: str
    last_name: str


class Mark(float, Enum):
    BARDZO_DOBRY = 5.0
    DOBRY_PLUS = 4.5
    DOBRY = 4.0
    DOSTATECZNY_PLUS = 3.5
    DOSTATECZNY = 3.0
    NIEDOSTATECZNY = 2.0