
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data
from model.users import users



professors = Table("professors", meta_data,
             Column("id_prof", Integer, primary_key=True),
             Column("id_user", Integer, ForeignKey(users.c.id_user), nullable=False),
             Column("name_prof", String(255), nullable=False),
             Column("last_name_prof", String(255), nullable=False))


meta_data.create_all(engine)