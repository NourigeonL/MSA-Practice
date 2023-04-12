import pytest
import unittest
from unittest import mock
import uuid
from src.services.orders_services import OrdersServices
from src.domain.orders import Order, OrderStatus, OrderCreate
from src.domain.id import ID
from src.exceptions.exceptions import OrderDoesNotExistException
from src.interfaces.services import IOrdersServices
class OrderServiceTest(unittest.TestCase):
  def setUp(self) -> None:
    self.repo = mock.Mock()
    self.service : IOrdersServices = OrdersServices(self.repo)

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
    self.repo.get_order.return_value = None
    with pytest.raises(OrderDoesNotExistException):
      self.service.get_order(code)

  def test_should_return_order(self):
    code = ID(1)
    expected = Order(code=code, product=ID(10), quantity=10, total=145.21, status=OrderStatus.PENDING)
    self.repo.get_order.return_value = expected
    order = self.service.get_order(code)
    assert order == expected

  def test_should_return_empty_list_when_product_does_not_exist(self):
    product_code = ID(45)
    self.repo.get_orders_of_product.return_value = []
    result = self.service.get_orders_of_product(product_code)
    self.repo.get_orders_of_product.assert_called_with(product_code)
    assert result == []

  def test_should_return_list_of_orders_of_a_product(self):
    product_code = ID(20)
    order2 = Order(code=ID(2), product=product_code, quantity=20, total=20.0, status=OrderStatus.PENDING)
    order1 = Order(code=ID(1), product=product_code, quantity=10, total=10.0, status=OrderStatus.PENDING)
    self.repo.get_orders_of_product.return_value = [order1, order2]
    result = self.service.get_orders_of_product(product_code)
    self.repo.get_orders_of_product.assert_called_with(product_code)
    assert order1 in result
    assert order2 in result

  def test_should_create_order(self):
    product_code = ID(uuid.uuid4())
    order_create = OrderCreate(product=product_code, quantity=50, total=12.23)
    expected = Order(code=ID(2), product = product_code, quantity=50, total=12.23, status=OrderStatus.PENDING)
    self.repo.add_order.return_value = expected
    order = self.service.create_order(order_create)
    self.repo.add_order.assert_called()
    assert order.code is not None
    assert order.status == OrderStatus.PENDING

  def test_should_change_order_status_to_cancelled(self):
    order = Order(code=ID(2), product = ID(uuid.uuid4()), quantity=50, total=12.23, status=OrderStatus.PENDING)
    self.service.verify_order(order)
    assert order.status == OrderStatus.CANCELLED
