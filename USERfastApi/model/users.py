from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

users = Table("users", meta_data, 
              Column("Id_user", Integer, primary_key=True),
              Column("Type_user", String(255), nullable=False),
              Column("password", String(255), nullable=False))

meta_data.create_all(engine)