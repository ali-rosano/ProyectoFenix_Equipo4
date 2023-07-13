
from fastapi import APIRouter
from schema.user_schema import UserSchema
from config.db import conn
from model.users import users
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get('/')
def root():
    return {"message": "Hi I am FastAPI with a Router"}

@user.post("/api/user")
def create_user(data_user: UserSchema):
    new_user = data_user.dict()
    new_user["password"] = f.encrypt(data_user.password.encode("utf-8"))
    conn.execute(users.insert().values(**new_user))
    conn.commit()
    return "Success"

@user.put("/api/user")
def update_user():
    pass