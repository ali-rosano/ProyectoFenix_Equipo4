from pydantic import BaseModel
from typing import Optional

class StudentSchema(BaseModel):
    id_student: Optional[int] = None
    id_user: int
    name_student: str
    last_name_student: str
    age: int
    phone_number: int
    email: str
    id_inscription: int