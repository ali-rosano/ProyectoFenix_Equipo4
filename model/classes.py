from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import engine, meta_data
from model.professors import professors

classes = Table(
    "classes",
    meta_data,
    Column("id_class", Integer, primary_key=True),
    Column("name_class", String(255), nullable=False),
    Column("level", String(255), nullable=False),
    Column("price", Float, nullable=False),
    Column("pack", String(255), nullable=False),
)

meta_data.create_all(engine)
