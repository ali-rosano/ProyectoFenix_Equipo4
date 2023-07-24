from sqlalchemy import select
from config.db import engine
from model.inscriptions import inscriptions
from model.classes import classes
from model.descuentos import descuentos
from model.descuentos_alumnos import descuentos_alumnos
from model.student import students
import logging
import pprint



def get_student_by_id_user(id_user: int):
    with engine.connect() as conn:
        result = conn.execute(
            students.select().where(students.c.id_user == id_user)
        ).first()

        return result
    
def get_class_by_id(class_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            classes.select().where(classes.c.id_class == class_id)).first()

        return result