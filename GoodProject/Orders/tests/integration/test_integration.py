import pytest
import unittest
from unittest import mock
from src.app import app
from fastapi.testclient import TestClient
from fastapi import status
from src.dependencies import get_order_service
from src.repositories.memrepo import OrderMemRepo
from src.services.orders_services import OrdersServices
from src.domain.id import ID
from src.domain.orders import Order, OrderCreate, OrderStatus
import uuid

class IntegrationTest(unittest.TestCase):
  def setUp(self) -> None:
    self.db = []
    self.repo = OrderMemRepo(self.db)
    self.service = OrdersServices(self.repo)
    app.dependency_overrides[get_order_service] = self.override_dependency
    self.client = TestClient(app)

  async def override_dependency(self):
        return self.service

  def test_should_return_all_orders(self):
     order1 = Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=45, total=45.2, status=OrderStatus.PENDING)
     order2 = Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=25, total=44.2, status=OrderStatus.CANCELLED)
     order3 = Order(code=ID(uuid.uuid4()), product=ID(uuid.uuid4()), quantity=65, total=4.2, status=OrderStatus.COMPLETED)
     self.db.extend([order1, order2, order3])

     response = self.client.get("/orders/")
     assert response.status_code == status.HTTP_200_OK
     assert response.json() == [order1.dict(), order2.dict(), order3.dict()]