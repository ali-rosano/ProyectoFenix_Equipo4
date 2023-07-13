from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    Id_user : Optional[str] = None
    Type_user : str
    password : str