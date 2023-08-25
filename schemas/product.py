from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    product_id: int
    name: str
    description: str
    price: float
    image: str
    category_id: int
    title: str
    discount: float


