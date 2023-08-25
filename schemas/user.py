from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    userid: Optional[int]
    username: str
    email: str
    password: str
    address: Optional[str]
    phone_number: Optional[str]
    role: Optional[int]
    status: Optional[int]

class UserCount(BaseModel):
    total: int
    