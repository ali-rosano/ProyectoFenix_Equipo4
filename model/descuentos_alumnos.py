from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data
from model.descuentos import descuentos
from model.student import students



descuentos_alumnos = Table("descuentos_alumnos", meta_data,
             Column("id_discount_student", Integer, primary_key=True),
             Column("id_discount", Integer, ForeignKey(descuentos.c.id_discount)),
             Column("id_student", Integer, ForeignKey(students.c.id_student)))


meta_data.create_all(engine)