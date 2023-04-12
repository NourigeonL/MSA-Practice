from src.interfaces.repositories import IOrderRepository
from src.domain.orders import Order
from src.domain.id import ID
from src.exceptions.exceptions import OrderDoesNotExistException

class OrderMemRepo(IOrderRepository):
  def __init__(self, db : list[Order]) -> None:
    self.db = db

  def get_orders(self) -> list[Order]:
      return self.db

  def get_order(self, code : ID) -> Order| None:
    for order in self.get_orders():
      if order.code == code:
        return order
    return None

  def add_order(self, order : Order) -> None:
    self.db.append(order)
    return order

  def get_orders_of_product(self, product : ID) -> list[Order]:
    res = []
    for order in self.get_orders():
      if order.product == product:
        res.append(order)
    return res