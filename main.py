import students
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(students.router, prefix="/students")

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000/",
    allow_credentials=True,
    allow_methods=["POST", "GET", "UPDATE", "DELETE"],
		allow_headers=["*"],
    max_age=3600,
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049)
