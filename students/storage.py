from functools import lru_cache

from .schema import Student

STUDENTS: dict[int, Student] = {}


@lru_cache(maxsize=1)
def get_students_storage() -> dict[int, Student]:
    return STUDENTS
