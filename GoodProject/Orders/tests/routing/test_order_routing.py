import pytest
import unittest
from unittest import mock
from fastapi.testclient import TestClient
import uuid
from src.app import app
from src.domain.orders import Order, OrderCreate
from src.dependencies import get_order_service
from src.exceptions.exceptions import ProductDoesNotExistException
class ProductRoute(unittest.TestCase):
    def setUp(self) -> None:
        self.service = mock.Mock()
        app.dependency_overrides[get_order_service] = self.override_dependency
        self.client = TestClient(app)

    async def override_dependency(self):
        return self.service