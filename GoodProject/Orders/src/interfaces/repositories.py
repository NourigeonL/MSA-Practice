import abc
from src.domain.orders import Order
from src.domain.id import ID
from typing import Any, List

class IOrderRepository(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def get_orders(self, filter : list[dict[str,any]] = None) -> list[Order]:
    raise NotImplementedError

  @abc.abstractmethod
  def get_order(self, code : ID) -> Order:
    raise NotImplementedError

  @abc.abstractmethod
  def add_order(self, order : Order) -> Order:
    raise NotImplementedError

  @abc.abstractmethod
  def save_changes(self) -> None:
    raise NotImplementedError

  @abc.abstractmethod
  def update_order(self, order : Order) -> None:
    raise NotImplementedError