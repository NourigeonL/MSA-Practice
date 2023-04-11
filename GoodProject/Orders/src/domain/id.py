from __future__ import annotations
from typing import Any
import uuid

class ID(str):
  def __new__(cls, val, *args, **kw):
    return str.__new__(cls,val, *args, **kw)
  def to_string(self):
    return super().__str__()
