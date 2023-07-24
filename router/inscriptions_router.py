from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.inscriptions_schema import InscriptionSchema
from config.db import engine
from model.inscriptions import inscriptions
from model.student import students
from typing import List
from business.discount_calculator import calculate_student_total_price
from business.student_price_updater import update_student_price


inscriptions_router = APIRouter()


@inscriptions_router.get("/api/inscriptions", response_model=List[InscriptionSchema])
def get_inscriptions():
    with engine.connect() as conn:
        result = conn.execute(inscriptions.select()).fetchall()

        return result


@inscriptions_router.get("/api/inscriptions/{inscription_id}", response_model=InscriptionSchema)
def get_inscription(inscription_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            inscriptions.select().where(inscriptions.c.id_inscription == inscription_id)
        ).first()

        return result


@inscriptions_router.post("/api/inscriptions", status_code=HTTP_201_CREATED)
def create_inscription(inscription_data: InscriptionSchema):
    with engine.connect() as conn:
        new_inscription = inscription_data.dict()
        conn.execute(inscriptions.insert().values(new_inscription))

        # Obtenemos el id_user (o student_id) de la inscripción
        student_id = new_inscription["id_user"]

        # Actualizamos el precio total del estudiante después de la inscripción
        #update_student_price(student_id)
        
        return {"message": "Inscription created successfully"}


@inscriptions_router.put("/api/inscriptions/{inscription_id}", response_model=InscriptionSchema)
def update_inscription(
    inscription_data: InscriptionSchema, inscription_id: int
):
    with engine.connect() as conn:
        conn.execute(
            inscriptions.update().values(inscription_data).where(
                inscriptions.c.id_inscription == inscription_id
            )
        )

        updated_inscription = conn.execute(
            inscriptions.select().where(
                inscriptions.c.id_inscription == inscription_id
            )
        ).first()

        return updated_inscription


@inscriptions_router.delete(
    "/api/inscriptions/{inscription_id}", status_code=HTTP_204_NO_CONTENT
)
def delete_inscription(inscription_id: int):
    with engine.connect() as conn:
        conn.execute(
            inscriptions.delete().where(
                inscriptions.c.id_inscription == inscription_id
            )
        )

        return {"message": "Inscription deleted successfully"}

