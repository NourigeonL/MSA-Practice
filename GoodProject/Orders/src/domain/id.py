from typing import Any

class ID(str):
  def __new__(cls, val, *args, **kw):
    return str.__new__(cls,val, *args, **kw)
  def to_string(self):
    return super().__str__()