from pydantic import BaseModel
from typing import Optional

class DiscountSchema(BaseModel):
    id_discount: Optional[int] = None
    discount_percent: Optional[int]
    discount_type: str
