import pytest
import unittest
import uuid
from src.domain.orders import Order, OrderStatus
from src.domain.id import ID

class OrderTest(unittest.TestCase):

  def test_init_order_model(self):
    order_code = ID(uuid.uuid4())
    product_code = ID(uuid.uuid4())
    quantity = 10
    total = 15.21
    status = OrderStatus.PENDING
    order = Order(code = order_code, product = product_code, quantity= quantity, total=total, status=status)

    assert order.code == order_code
    assert order.product == product_code
    assert order.quantity == quantity
    assert order.total == total
    assert order.status == status

  def test_init_order_model_from_dict(self):
    code = ID(uuid.uuid4())
    product_code = ID(uuid.uuid4())
    init_dict = {
      "code": code,
      "product": product_code,
      "quantity": 50,
      "total": 45.1,
      "status": OrderStatus.PENDING
    }

    order = Order.parse_obj(init_dict)
    assert order.code == code
    assert order.product == product_code
    assert order.quantity == 50
    assert order.total == 45.1
    assert order.status == OrderStatus.PENDING

  def test_order_model_to_dict(self):
    code = ID(uuid.uuid4())
    product_code = ID(uuid.uuid4())
    init_dict = {
    "code": code,
    "product": product_code,
    "quantity": 50,
    "total": 45.1,
    "status": OrderStatus.PENDING
    }
    order = Order.parse_obj(init_dict)
    assert order.dict() == init_dict

  def test_order_model_comparaison(self):
    code = ID(uuid.uuid4())
    product_code = ID(uuid.uuid4())
    order1 = Order(code = code, product = product_code, quantity= 50, total=45.2, status=OrderStatus.PENDING)
    order2 = Order(code = code, product = product_code, quantity= 50, total=45.2, status=OrderStatus.PENDING)

    assert order1 == order2
