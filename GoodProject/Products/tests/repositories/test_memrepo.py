import pytest
import uuid
import unittest
from unittest import mock
from src.domain.product import Product
from src.repositories.memrepo import MemRepo
from src.exceptions.exceptions import ProductDoesNotExistException

@pytest.fixture
def product_dicts():
  return [
    Product(
    code=str(uuid.uuid4()),
    name="Product 1",
    price=1.1,
    quantity=10
  ).dict(),
  Product(
    code=str(uuid.uuid4()),
    name="Product 2",
    price=2.2,
    quantity=20
  ).dict(),
  Product(
    code=str(uuid.uuid4()),
    name="Product 3",
    price=3.3,
    quantity=30
  ).dict(),
  Product(
    code=str(uuid.uuid4()),
    name="Product 4",
    price=4.4,
    quantity=40
  ).dict()
  ]

def test_repository_list_without_parameters(product_dicts):
  repo = MemRepo(product_dicts)
  products = [Product.parse_obj(product_dict) for product_dict in product_dicts]
  assert repo.get_products() == products

def test_repository_throw_product_does_not_exist_error_when_product_not_found():
  repo = MemRepo([])
  with pytest.raises(ProductDoesNotExistException):
    repo.get_product(str(uuid.uuid4()))

def test_return_the_right_product(product_dicts):
  code_product = str(uuid.uuid4())
  expected = Product(code=code_product, name="Product", quantity=50, price=2.35)
  repo = MemRepo([expected.dict()])
  product = repo.get_product(code_product)
  assert product == expected

def test_should_create_product():
  expected = Product(code=str(uuid.uuid4()), name="Product1", quantity=12, price=12.6)
  db = []
  repo = MemRepo(db)
  product : Product = repo.create_product(expected)
  assert product == expected