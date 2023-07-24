from pydantic import BaseModel
from typing import Optional
from datetime import date

class InscriptionSchema(BaseModel):
    id_inscription: Optional[int] = None
    id_user: int
    id_class: int
    type_inscription: str
    status: bool
    start_date: Optional[date] = None
    finish_date: Optional[date] = None
