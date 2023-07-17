from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data


descuentos = Table("descuentos", meta_data,
             Column("id_discount", Integer, primary_key=True),
             Column("discount_percent", Integer),
             Column("discount_type", String(255)))


meta_data.create_all(engine)