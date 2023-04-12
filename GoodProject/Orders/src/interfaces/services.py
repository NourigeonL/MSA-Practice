import abc
from src.domain.orders import Order, OrderCreate
from src.domain.id import ID

class IOrdersServices(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def get_orders(self) -> list[Order]:
    raise NotImplementedError

  @abc.abstractmethod
  def get_order(self, code: ID) -> Order:
    raise NotImplementedError

  @abc.abstractmethod
  def get_orders_of_product(self, product_code: ID) -> list[Order]:
    raise NotImplementedError

  @abc.abstractmethod
  def create_order(self, order_create : OrderCreate) -> Order:
    raise NotImplementedError

  @abc.abstractmethod
  def verify_order(self, order : Order, quantity : int) -> None:
    raise NotImplementedError
