import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == {}


def test_create_student():
    response = client.post(
        "/students",
        json={"first_name": "Karol", "last_name": "Krotkowski"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "student_id": 1,
        "first_name": "Karol",
        "last_name": "Krotkowski",
    }


def test_create_student_missing_data():
    response = client.post(
        "/students", json={"first_name": "", "last_name": "Krotkowski"}
    )
    assert response.status_code == 422
    assert response.json() == {"detail": "Empty student data"}


def test_create_and_get_3_students():
    client.post("/students", json={"first_name": "Karol", "last_name": "Krotkowski"})
    client.post("/students", json={"first_name": "Ala", "last_name": "Orta"})
    client.post("/students", json={"first_name": "Marcin", "last_name": "Liga"})

    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == {
        "1": {"student_id": 1, "first_name": "Karol", "last_name": "Krotkowski"},
        "2": {"student_id": 2, "first_name": "Ala", "last_name": "Orta"},
        "3": {"student_id": 3, "first_name": "Marcin", "last_name": "Liga"},
    }


def test_update_student_data():
    client.post("/students", json={"first_name": "Karol", "last_name": "Krotkowski"})

    response = client.put(
        "/students/1", json={"first_name": "Lidia", "last_name": "Sobialska"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "student_id": 1,
        "first_name": "Lidia",
        "last_name": "Sobialska",
    }


def test_delete_student():
    client.post("/students", json={"first_name": "Karol", "last_name": "Krotkowski"})

    response = client.delete("/students/1")
    assert response.status_code == 200
    assert response.json() == {"Student deleted": True}


def test_delete_nonexistent_student():
    response = client.delete("/students/10")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}


def test_create_mark():
    client.post(
        "/students",
        json={"first_name": "Karol", "last_name": "Krotkowski"},
    )

    response = client.post(
        "/students/1/marks/4"
    )
    assert response.status_code == 200
    assert response.json() == 4


def test_create_mark_with_incorrect_format():
    client.post(
        "/students",
        json={"first_name": "Karol", "last_name": "Krotkowski"},
    )

    response = client.post(
        "/students/1/marks/1"
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": 
        [{'ctx': {'enum_values': [5.0, 4.5, 4.0, 3.5, 3.0, 2.0]}, 
          'loc': ['path', 'mark'], 
          'msg': 'value is not a valid enumeration member; permitted: 5.0, 4.5, 4.0, 3.5, 3.0, 2.0', 
          'type': 'type_error.enum'}]
    }


def test_create_mark_for_nonexistent_student():
    response = client.post("/students/5/marks/4")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}


@pytest.fixture(autouse=True)
def delete_all_students():
    students = client.get("/students").json()
    for student in students.values():
        client.delete(f"/students/{student['student_id']}")
