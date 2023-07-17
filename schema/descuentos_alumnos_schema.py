from pydantic import BaseModel
from typing import Optional

class DescuentoAlumnoSchema(BaseModel):
    id_discount_student: Optional[int] = None
    id_discount: Optional[int]
    id_student: int