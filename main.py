import students
import uvicorn

from fastapi import FastAPI

app = FastAPI()

app.include_router(students.router, prefix="/students")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049)
