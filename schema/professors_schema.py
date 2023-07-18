from pydantic import BaseModel
from typing import Optional

class ProfessorSchema(BaseModel):
    id_prof: Optional[int] = None
    id_user: int
    name_prof: str
    last_name_prof: str
