import pytest
import uuid

from src.domain.product import Product
from src.repository.memrepo import MemRepo

@pytest.fixture
def product_dicts():
  return [
    Product(
    code=uuid.uuid4(),
    name="Product 1",
    price=1.1,
    quantity=10
  ).dict(),
  Product(
    code=uuid.uuid4(),
    name="Product 2",
    price=2.2,
    quantity=20
  ).dict(),
  Product(
    code=uuid.uuid4(),
    name="Product 3",
    price=3.3,
    quantity=30
  ).dict(),
  Product(
    code=uuid.uuid4(),
    name="Product 4",
    price=4.4,
    quantity=40
  ).dict()
  ]

def test_repository_list_without_parameters(product_dicts):
  repo = MemRepo(product_dicts)
  products = [Product.parse_obj(product_dict) for product_dict in product_dicts]
  assert repo.list() == products