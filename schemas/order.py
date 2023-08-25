import string
from pydantic import BaseModel
from typing import Optional


from datetime import date

class Order(BaseModel):
    order_id: int
    userid: Optional[int]
    staff_id: Optional[int]
    state: Optional[int] 
    total: Optional[float]
    orderDate: date
    product_id: int
    quantity: Optional[int]



