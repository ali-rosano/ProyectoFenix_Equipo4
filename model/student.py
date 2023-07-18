from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data
from model.users import users
from model.inscriptions import inscriptions

students = Table("students", meta_data,
             Column("id_student", Integer, primary_key=True),
             Column("id_user", Integer, ForeignKey(users.c.id_user), nullable=False),
             Column("name_student", String(255), nullable=False),
             Column("last_name_student", String(255), nullable=False),
             Column("age", Integer, nullable=False),
             Column("phone_number", Integer, nullable=False),
             Column("email", String(255), nullable=False),
             Column("id_inscription", Integer, ForeignKey(inscriptions.c.id_inscription), nullable=False))


meta_data.create_all(engine)
