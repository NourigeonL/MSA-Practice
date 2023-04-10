import pytest
import unittest
from unittest import mock
import uuid
from src.services.orders_services import OrdersServices
from src.domain.orders import Order, OrderStatus, OrderCreate
from src.domain.id import ID
from src.exceptions.exceptions import OrderDoesNotExistException
class OrderServiceTest(unittest.TestCase):
  def setUp(self) -> None:
    self.repo = mock.Mock()
    self.service = OrdersServices(self.repo)

  def test_should_return_list(self):
    self.repo.get_orders.return_value = []
    orders = self.service.get_orders()
    assert isinstance(orders, list)

  def test_should_return_orders(self):
    order1 = Order(code=ID(1), product=ID(10), quantity=10, total=145.21, status=OrderStatus.PENDING)
    order2 = Order(code=ID(2), product=ID(20), quantity=20, total=245.21, status=OrderStatus.PENDING)
    self.repo.get_orders.return_value = [order1, order2]
    orders = self.service.get_orders()
    assert orders == [order1, order2]

  def test_should_raise_order_does_not_exist_error(self):
    code = ID(45)
    self.repo.get_order.side_effect = OrderDoesNotExistException(code=code)
    with pytest.raises(OrderDoesNotExistException):
      self.service.get_order(code)

  def test_should_return_order(self):
    code = ID(1)
    expected = Order(code=code, product=ID(10), quantity=10, total=145.21, status=OrderStatus.PENDING)
    self.repo.get_order.return_value = expected
    order = self.service.get_order(code)
    assert order == expected
