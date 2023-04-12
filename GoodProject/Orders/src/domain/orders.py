from __future__ import annotations
from pydantic import BaseModel
from enum import Enum
from .id import ID

class OrderStatus(str, Enum):
  PENDING = "pending"
  CANCELLED = "cancelled"
  COMPLETED = "completed"

class Order(BaseModel):
  code: ID
  product: ID
  quantity: int
  total: float
  status : OrderStatus

  class Config:
        use_enum_values = True

class OrderCreate(BaseModel):
  product: ID
  quantity: int
  total: float