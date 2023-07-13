from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:admin@localhost:3306/proyectofenix")

conn = engine.connect()

meta_data = MetaData()