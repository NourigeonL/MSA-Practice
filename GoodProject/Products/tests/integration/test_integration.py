import pytest
import unittest
from unittest import mock
from src.dependencies import get_product_service
from src.repositories.memrepo import MemRepo
from src.services.products_services import ProductService
from fastapi.testclient import TestClient
from src.app import app
from src.domain.product import Product
import uuid
class IntegrationTest(unittest.TestCase):
  def setUp(self) -> None:
    self.db = []
    self.repo = MemRepo(self.db)
    self.service = ProductService(self.repo)
    app.dependency_overrides[get_product_service] = self.override_dependency
    self.client = TestClient(app)

  async def override_dependency(self):
        return self.service

  def test_should_return_all_products(self):
    code1 = str(uuid.uuid4())
    code2 = str(uuid.uuid4())
    product1 = Product(code=code1, name="Product1", quantity=50, price=2.68)
    product2 = Product(code=code2, name="Product2", quantity=30, price=2.28)
    self.db.extend([product1.dict(), product2.dict()])

    response = self.client.get("/products")
    assert response.status_code == 200
    assert response.json() == [product1.dict(), product2.dict()]

  def test_should_return_product_two(self):
    code1 = str(uuid.uuid4())
    code2 = str(uuid.uuid4())
    product1 = Product(code=code1, name="Product1", quantity=50, price=2.68)
    product2 = Product(code=code2, name="Product2", quantity=30, price=2.28)
    self.db.extend([product1, product2])
    response = self.client.get(f"/products/{code2}")
    assert response.status_code == 200
    assert response.json() == product2.dict()

  def test_should_create_product(self):
     response = self.client.post("/products",json={"name":"ProductCreate", "quantity": 23, "price": 23.2})
     assert response.status_code == 201
     assert len(self.db) == 1
     product_dict = response.json()
     product = Product.parse_obj(product_dict)
     assert product_dict == self.db[0]
     assert product.code is not None
     assert product.name == "ProductCreate"
     assert product.quantity == 23
     assert product.price == 23.2