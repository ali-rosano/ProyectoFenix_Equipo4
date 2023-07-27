from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import UserSchema, DataUser
from config.db import engine
from model.users import users
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from logger.logger import log_critical, log_debug, log_error, log_info, log_warning
from sqlalchemy import text
from config.config import settings

user = APIRouter()

@user.get("/")
def root():
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {settings.MYSQL_DB};"))
        log_info("Inicio de la Api correcto")
    return ("Message : Soy Api con Router")

@user.get("/api/user", response_model=List[UserSchema])
def get_users():
    with engine.connect() as conn:
        log_info("conexion correcta")
        result = conn.execute(users.select()).fetchall()

        return result
    
@user.get("/api/user/{user_id}", response_model=UserSchema)
def get_user(user_id: str):  
    with engine.connect() as conn:
        log_info("conexion correcta en la solicitud de muestra de usuario especifico")
        result = conn.execute(users.select().where(users.c.id_user == user_id)).first()

        return result

@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    with engine.connect() as conn:
        log_info("conexion correcta en la solicitud de agregar un usuario nuevo")
        new_user = data_user.dict()
        new_user["password"] = generate_password_hash(data_user.password, "pbkdf2:sha256:30", 
        30)
        
        conn.execute(users.insert().values(new_user))
        return Response(status_code=HTTP_201_CREATED)
    
@user.post("/api/user/login", status_code=200)
def user_login(data_user: DataUser):
    with engine.connect() as conn:
        log_info("conexion correcta para accesos de usuario")
        result = conn.execute(users.select().where(users.c.type_user == data_user.type_user)).first()
        
        if result != None:
            check_password = check_password_hash(result[2], data_user.password)
            
            if check_password:
              return {
                  "status": 200,
                  "message": "Access success"
              } 
            
        return {
            "status": HTTP_401_UNAUTHORIZED,
            "message": "Access denied"
        }


@user.put("/api/user/{user_id}", response_model=UserSchema)
def update_user(data_update: UserSchema, user_id: str):
    with engine.connect() as conn:
        log_info("conexion correcta para la actualizacion de usuario especifico")
        encryp_password = generate_password_hash(data_update.password, "pbkdf2:sha256:30", 
        30)

        conn.execute(users.update().values(id_user=data_update.id_user, type_user=data_update.type_user, 
        password=encryp_password).where(users.c.id_user == user_id))

        result = conn.execute(users.select().where(users.c.id_user == user_id)).first()

        return result
    
@user.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    with engine.connect() as conn:
            log_info("conexion correcta para la eliminacion de usuario especifico")
            conn.execute(users.delete().where(users.c.id_user == user_id))

            return Response (status_code=HTTP_204_NO_CONTENT)