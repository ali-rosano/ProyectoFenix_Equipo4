from pydantic import BaseModel
from typing import Optional

class ClassSchema(BaseModel):
    id_class: Optional[int] = None
    name_class: str
    level: str
    price: float
    pack: str
    id_prof: int

