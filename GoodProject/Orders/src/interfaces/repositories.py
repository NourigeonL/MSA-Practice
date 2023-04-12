import abc
from src.domain.orders import Order
from src.domain.id import ID
from typing import Any, List

class IOrderRepository(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def get_orders(self, filters : list[dict[str,any]] = None) -> list[Order]:
    raise NotImplementedError

  @abc.abstractmethod
  def get_orders_of_product(self, product : ID) -> list[Order]:
    raise NotImplementedError

  @abc.abstractmethod
  def get_order(self, code : ID) -> Order| None:
    raise NotImplementedError

  @abc.abstractmethod
  def add_order(self, order : Order) -> None:
    raise NotImplementedError