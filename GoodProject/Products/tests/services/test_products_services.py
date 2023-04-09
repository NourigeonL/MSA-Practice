import pytest
import uuid
from unittest import mock

from src.domain.product import Product
from src.services.products import ProductService

@pytest.fixture
def domain_products():
  product_1 = Product(
    code=uuid.uuid4(),
    name="Product 1",
    price=1.1,
    quantity=10
  )
  product_2 = Product(
    code=uuid.uuid4(),
    name="Product 2",
    price=2.2,
    quantity=20
  )
  product_3 = Product(
    code=uuid.uuid4(),
    name="Product 3",
    price=3.3,
    quantity=30
  )
  product_4 = Product(
    code=uuid.uuid4(),
    name="Product 4",
    price=4.4,
    quantity=40
  )

  return [product_1,product_2,product_3,product_4]

def test_product_list_without_parameters(domain_products):
  repo = mock.Mock()
  product_service = ProductService(repo)
  repo.get_products.return_value = domain_products

  result = product_service.get_products()

  repo.get_products.assert_called_with()
  assert result == domain_products