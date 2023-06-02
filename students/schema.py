from pydantic import BaseModel


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
