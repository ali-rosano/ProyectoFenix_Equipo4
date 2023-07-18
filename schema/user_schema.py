from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id_user: Optional[int] = None
    type_user: str
    password: str

class DataUser(BaseModel):
    type_user: str
    password: str