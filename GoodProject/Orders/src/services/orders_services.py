from src.interfaces.services import IOrdersServices
from src.interfaces.repositories import IOrderRepository
from src.domain.orders import Order, OrderCreate, OrderStatus
from src.domain.id import ID
from src.exceptions.exceptions import OrderDoesNotExistException
import uuid
class OrdersServices(IOrdersServices):
  def __init__(self, repo : IOrderRepository) -> None:
    self._repo = repo

  def get_orders(self) -> list[Order]:
    return self._repo.get_orders()

  def get_order(self, code: ID) -> Order:
    order = self._repo.get_order(code)
    if order is None:
      raise OrderDoesNotExistException(code=code)
    return order

  def get_orders_of_product(self, product_code: ID) -> list[Order]:
    return self._repo.get_orders_of_product(product_code)

  def create_order(self, order_create : OrderCreate) -> Order:
    code = ID(uuid.uuid4())
    order = Order(code=code, product=order_create.product, quantity=order_create.quantity, total=order_create.total, status=OrderStatus.PENDING)
    self._repo.add_order(order)
    return order

  def verify_order(self, order : Order, quantity : int) -> None:
    print(order, quantity)
    new_order = self.get_order(order.code)
    new_order.status = OrderStatus.COMPLETED if order.quantity == quantity else OrderStatus.CANCELLED
    print(new_order)