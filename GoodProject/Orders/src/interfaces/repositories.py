import abc
from src.domain.orders import Order
from src.domain.id import ID
class IOrderRepository(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def get_orders(self) -> list[Order]:
    raise NotImplementedError

  @abc.abstractmethod
  def get_order(self, code : ID) -> Order:
    raise NotImplementedError

  @abc.abstractmethod
  def create_order(self, order : Order) -> Order:
    raise NotImplementedError