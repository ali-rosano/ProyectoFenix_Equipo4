from fastapi import APIRouter, HTTPException
from sqlalchemy import select, update
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.class_schema import ClassSchema
from config.db import engine
from model.classes import classes
from typing import List
from logger.logger import log_critical


classes_router = APIRouter()


@classes_router.get("/api/classes", response_model=List[ClassSchema])
def get_classes():
    with engine.connect() as conn:
        result = conn.execute(classes.select()).fetchall()

        return result


@classes_router.get(
    "/api/classes/{class_id}", response_model=ClassSchema
)
def get_class(class_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            classes.select().where(classes.c.id_class == class_id)).first()

        return result


@classes_router.post("/api/classes", status_code=HTTP_201_CREATED)
def create_class(class_data: ClassSchema):
    with engine.connect() as conn:
        new_class = class_data.dict()
        conn.execute(classes.insert().values(new_class))

        return {"message": "Class created successfully"}


@classes_router.put("/api/classes/{class_id}", response_model=ClassSchema)

def update_class(class_data: ClassSchema, class_id: int):

    updated_data = class_data.dict()

    with engine.connect() as conn:
        conn.execute(
            classes.update().values(**updated_data).where(
                classes.c.id_class == class_id
            )
        )

        updated_class = conn.execute(
            classes.select().where(classes.c.id_class == class_id)
        ).first()

        return updated_class


@classes_router.delete("/api/classes/{class_id}", status_code=HTTP_204_NO_CONTENT)
def delete_class(class_id: int):
    with engine.connect() as conn:
        conn.execute(classes.delete().where(classes.c.id_class == class_id))

        return {"message": "Class deleted successfully"}

"""
@classes_router.put("/api/classes/{class_id}/assign_professor/{professor_id}")
def assign_professor_to_class(class_id: int, professor_id: int):
    with engine.connect() as conn:
        conn.execute(
            classes.update()
            .values(professor_id=professor_id)
            .where(classes.c.id_class == class_id)
        )

        return {"message": "Professor assigned to class successfully"}
"""