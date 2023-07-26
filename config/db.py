from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root@localhost:3306/proyectofenix2")

engine.execute(f"CREATE DATABASE IF NOT EXISTS proyectofenix2;")

meta_data = MetaData()