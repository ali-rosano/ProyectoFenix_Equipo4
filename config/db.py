from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Youlye1012.@localhost:3306/proyectofenix")

meta_data = MetaData()