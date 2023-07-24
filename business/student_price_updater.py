from sqlalchemy import select, update
from config.db import engine
from model.student import students
from business.discount_calculator import calculate_student_total_price
import logging
import pprint

def update_student_price(student_id: int):
    # Calcular el nuevo precio total con descuentos para el estudiante
    logging.info("voy a calcular el precio")
    new_total_price = calculate_student_total_price(student_id)
    logging.info(f"Precio total a actualizar: {new_total_price}")
    # Actualizar el precio total del estudiante en la tabla 'students'
    with engine.connect() as conn:
        stmt = update(students).where(students.c.id_student == student_id).values(Total_price=new_total_price)
        conn.execute(stmt)

    # Devuelve el estudiante actualizado
        updated_student = conn.execute(select([students]).where(students.c.id_student == student_id)).first()
        
        logging.info(pprint.pformat(updated_student))
        return updated_student
