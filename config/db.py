from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:admin@localhost:3306/proyectofenix")

meta_data = MetaData()