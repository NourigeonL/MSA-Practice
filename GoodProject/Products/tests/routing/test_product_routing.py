import pytest
import unittest
from unittest import mock
from fastapi.testclient import TestClient
import uuid
from src.app import app
from src.domain.product import Product, ProductCreate
from src.dependencies import get_product_service
from src.exceptions.exceptions import ProductDoesNotExistException
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

    def test_return_not_found_when_get_product_not_found(self):
        code = str(uuid.uuid4())
        self.service.get_product.side_effect = ProductDoesNotExistException(code=code)
        response = self.client.get(f"/products/{code}")
        self.service.get_product.assert_called_with(code)
        assert response.status_code == 404

    def test_should_return_product(self):
        code = str(uuid.uuid4())
        product = Product(code=code, name="Product1", price=12.2, quantity=50)
        self.service.get_product.return_value = product
        response = self.client.get(f"/products/{code}")
        self.service.get_product.assert_called_with(code)
        assert response.status_code == 200
        assert response.json() == product.dict()

    def test_should_create_product(self):
        product = Product(code=str(uuid.uuid4()), name="Test Product", price=2.3, quantity=50)
        self.service.create_product.return_value = product
        product_create = ProductCreate(name="Test Product", price=2.3, quantity=50)
        response = self.client.post("/products/", json=product_create.dict())
        assert response.status_code == 201
        assert response.json() == product.dict()
