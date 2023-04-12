import pytest
import unittest
from unittest import mock
from src.repositories.memrepo import OrderMemRepo
from src.domain.orders import Order, OrderStatus
from src.domain.id import ID
import uuid

class OrderMemRepoTest(unittest.TestCase):

  def test_should_return_empty_list(self):
    db = []
    repo = OrderMemRepo(db)
    orders = repo.get_orders()
    assert orders == []

  def test_should_return_all_orders(self):
    order1 = Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    order2 =  Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    order3 =  Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    db = [order1, order2, order3]
    repo = OrderMemRepo(db)
    orders = repo.get_orders()
    assert len(orders) == 3
    assert isinstance(orders[0], Order)

  def test_should_return_all_order_of_product(self):
    product_id = ID(uuid.uuid4())
    order1 = Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    order2 =  Order(code=ID(uuid.uuid4()), product=product_id, quantity=20, total=12.45, status=OrderStatus.PENDING)
    order3 =  Order(code=ID(uuid.uuid4()), product=product_id, quantity=20, total=12.45, status=OrderStatus.PENDING)
    db = [order1, order2, order3]
    repo = OrderMemRepo(db)
    orders = repo.get_orders_of_product(product_id)
    assert orders == [order2, order3]

  def test_should_return_one_order(self):
    order1 = Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    order2 =  Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    order3 =  Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    db = [order1, order2, order3]
    repo = OrderMemRepo(db)
    order = repo.get_order(order2.code)
    assert isinstance(order, Order)
    assert order == order2

  def test_should_return_none_when_order_does_not_exist(self):
    code = ID(uuid.uuid4())
    order1 = Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    order2 =  Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    order3 =  Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    db = [order1, order2, order3]
    repo = OrderMemRepo(db)
    order = repo.get_order(code)
    assert order is None

  def test_should_add_order(self):
    db = []
    order1 = Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.45, status=OrderStatus.PENDING)
    repo = OrderMemRepo(db)
    repo.add_order(order1)
    assert db == [order1]