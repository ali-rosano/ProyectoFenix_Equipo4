from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.students_schema import StudentSchema 
from config.db import engine
from model.student import students
from typing import List

student_router = APIRouter()


@student_router.get("/api/students", response_model=List[StudentSchema])
def get_students():
    with engine.connect() as conn:
        result = conn.execute(students.select()).fetchall()

        return result


@student_router.get("/api/students/{student_id}", response_model=StudentSchema)
def get_student(student_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            students.select().where(students.c.id_student == student_id)
        ).first()

        return result


@student_router.post("/api/students", status_code=HTTP_201_CREATED)
def create_student(student_data: StudentSchema):
    with engine.connect() as conn:
        new_student = student_data.dict()
        conn.execute(students.insert().values(new_student))

        return {"message": "Student created successfully"}


@student_router.put("/api/students/{student_id}", response_model=StudentSchema)
def update_student(student_data: StudentSchema, student_id: int):
    with engine.connect() as conn:
        conn.execute(
            students.update().values(student_data).where(
                students.c.id_student == student_id
            )
        )

        updated_student = conn.execute(
            students.select().where(students.c.id_student == student_id)
        ).first()

        return updated_student


@student_router.delete("/api/students/{student_id}", status_code=HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    with engine.connect() as conn:
        conn.execute(students.delete().where(students.c.id_student == student_id))

        return {"message": "Student deleted successfully"}
