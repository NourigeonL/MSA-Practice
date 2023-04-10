import uuid
import dataclasses
from pydantic import BaseModel


class Product(BaseModel):
  code: str
  name: str
  quantity: int
  price: float

class ProductCreate(BaseModel):
  name: str
  quantity: int
  price: float