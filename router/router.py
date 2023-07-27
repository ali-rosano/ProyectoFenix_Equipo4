
from fastapi import APIRouter, Response, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import UserSchema, DataUser
from config.db import engine
from model.users import users
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from tags import tags_metadata

user = APIRouter()


@user.get("/")
def root():
    return {"Bienvenido a la  API de Danza Fénix"}

@user.get("/api/user", tags=["users"], response_model=List[UserSchema])
def get_users():
    try:
        with engine.connect() as conn:
            result = conn.execute(users.select()).fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong")


@user.get("/api/user/{user_id}", tags=["users"], response_model=UserSchema)
def get_user(user_id: str):
    try:
        with engine.connect() as conn:
            result = conn.execute(users.select().where(users.c.id_user == user_id)).first()
        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong")


@user.post("/api/user", tags=["users"], status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    try:
        with engine.connect() as conn:
            new_user = data_user.dict()
            new_user["password"] = generate_password_hash(data_user.password, "pbkdf2:sha256:30", 30)
            conn.execute(users.insert().values(new_user))
        return Response(status_code=HTTP_201_CREATED)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong")


@user.post("/api/user/login", tags=["users"], status_code=200)
def user_login(data_user: DataUser):
    try:
        with engine.connect() as conn:
            result = conn.execute(users.select().where(users.c.type_user == data_user.type_user)).first()
            if result is not None:
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
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong")


@user.put("/api/user/{user_id}", tags=["users"], response_model=UserSchema)
def update_user(data_update: UserSchema, user_id: str):
    try:
        with engine.connect() as conn:
            encryp_password = generate_password_hash(data_update.password, "pbkdf2:sha256:30", 30)
            conn.execute(users.update().values(id_user=data_update.id_user, type_user=data_update.type_user,
                                                password=encryp_password).where(users.c.id_user == user_id))
            result = conn.execute(users.select().where(users.c.id_user == user_id)).first()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong")


@user.delete("/api/user/{user_id}", tags=["users"], status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    try:
        with engine.connect() as conn:
            conn.execute(users.delete().where(users.c.id_user == user_id))
        return Response(status_code=HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong")