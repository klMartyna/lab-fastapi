from functools import lru_cache

from .schema import Student

STUDENTS: dict[int, Student] = {1 : {"student_id": 1, "first_name": "Ala", "last_name": "Orta"}, 2: {"student_id": 2, "first_name": "Marcin", "last_name": "Liga"}}


@lru_cache(maxsize=1)
def get_students_storage() -> dict[int, Student]:
    return STUDENTS
