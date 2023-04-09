import uuid
import dataclasses
from pydantic import BaseModel


class Product(BaseModel):
  code: uuid.UUID
  name: str
  quantity: int
  price: float
