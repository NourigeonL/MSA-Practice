import pytest
import unittest
from unittest import mock
from fastapi.testclient import TestClient
from src.services.products import ProductService
import uuid
import json
from src.main import app
from src.domain.product import Product
from src.dependencies import get_product_service

class ProductRoute(unittest.TestCase):
    def setUp(self) -> None:
        self.service = mock.Mock()
        app.dependency_overrides[get_product_service] = self.override_dependency
        self.client = TestClient(app)

    async def override_dependency(self):
        return self.service

    def test_list_products(self):
        product_dict = {
        "code": str(uuid.uuid4()),
        "name": "Product1",
        "price": 23.2,
        "quantity": 50
        }

        products = [Product.parse_obj(product_dict)]

        self.service.get_products.return_value = products


        response = self.client.get("/products")
        print(response.json())

        self.service.get_products.assert_called()

        assert response.status_code == 200
        assert response.json() == [product_dict]