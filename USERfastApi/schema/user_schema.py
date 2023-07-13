from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    Id_user : Optional[str]
    Type_user : str
    password : str