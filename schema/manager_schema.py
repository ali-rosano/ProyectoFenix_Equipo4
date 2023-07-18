from pydantic import BaseModel
from typing import Optional

class ManagerSchema(BaseModel):
    id_mana: Optional[int] = None
    id_user: int
    name_mana: str
    last_name_mana: str