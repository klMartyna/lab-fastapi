from functools import lru_cache
from collections import defaultdict

from .schema import Student, Mark

STUDENTS: dict[int, Student] = {}
MARKS: dict[int, list[Mark]] = defaultdict(list)


@lru_cache(maxsize=1)
def get_students_storage() -> dict[int, Student]:
    return STUDENTS
