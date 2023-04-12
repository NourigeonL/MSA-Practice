import pytest
import unittest
from unittest import mock
from fastapi.testclient import TestClient
import uuid
from fastapi import status
from src.app import app
from src.domain.orders import Order, OrderCreate, OrderStatus
from src.domain.id import ID
from src.dependencies import get_order_service
from src.exceptions.exceptions import OrderDoesNotExistException
class ProductRoute(unittest.TestCase):
    def setUp(self) -> None:
        self.service = mock.Mock()
        app.dependency_overrides[get_order_service] = self.override_dependency
        self.client = TestClient(app)

    async def override_dependency(self):
        return self.service

    def test_should_return_all_orders(self):
        order1 = Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=20, total=12.2, status=OrderStatus.PENDING)
        order2 = Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=10, total=22.2, status=OrderStatus.PENDING)
        self.service.get_orders.return_value = [order1, order2]
        response = self.client.get("/orders")
        assert response.status_code == 200
        assert response.json() == [order1.dict(), order2.dict()]

    def test_should_return_order(self):
        code = ID(uuid.uuid4())
        order = Order(code=code, product=ID(uuid.uuid4()), quantity=20, total=12.2, status=OrderStatus.PENDING)
        self.service.get_order.return_value = order
        response = self.client.get(f"/orders/{code}")
        self.service.get_order.assert_called_with(code=code)
        assert response.status_code == 200
        assert response.json() == order.dict()

    def test_should_return_not_found(self):
        code = ID(uuid.uuid4())
        self.service.get_order.side_effect = OrderDoesNotExistException(code=code)
        response = self.client.get(f"/orders/{code}")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == None

    def test_should_create_order(self):
        product = ID(uuid.uuid4())
        order_create = OrderCreate(product=product, quantity=50, total=12.23)
        expected = Order(code=ID(uuid.uuid4()), product=product, quantity=50, total=12.23, status=OrderStatus.PENDING)
        self.service.create_order.return_value = expected
        response = self.client.post("/orders/", json=order_create.dict())
        self.service.create_order.assert_called_with(order_create)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == expected.dict()

    def test_should_return_orders_of_product(self):
        product = ID(uuid.uuid4())
        order1 = Order(code=ID(uuid.uuid4()), product=product, quantity=50, total=12.23, status=OrderStatus.PENDING)
        order2 = Order(code=ID(uuid.uuid4()), product=product, quantity=30, total=11.23, status=OrderStatus.PENDING)

        self.service.get_orders_of_product.return_value = [order1,order2]
        response = self.client.get(f"/products/{product}/orders")
        self.service.get_orders_of_product.assert_called_with(product)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [order1.dict(), order2.dict()]
