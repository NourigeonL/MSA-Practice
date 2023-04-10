from src.interfaces.services import IOrdersServices
from src.interfaces.repositories import IOrderRepository
from src.domain.orders import Order
from src.domain.id import ID
from src.exceptions.exceptions import OrderDoesNotExistException
class OrdersServices(IOrdersServices):
  def __init__(self, repo : IOrderRepository) -> None:
    self._repo = repo

  def get_orders(self) -> list[Order]:
    return self._repo.get_orders()

  def get_order(self, code: ID) -> Order:

    return self._repo.get_order(code)