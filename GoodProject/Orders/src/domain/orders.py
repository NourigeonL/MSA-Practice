from __future__ import annotations
from pydantic import BaseModel
from enum import Enum
from .id import ID

class OrderStatus(Enum):
  PENDING = 0

class Order(BaseModel):
  code: ID
  product: ID
  quantity: int
  total: float
  status : OrderStatus