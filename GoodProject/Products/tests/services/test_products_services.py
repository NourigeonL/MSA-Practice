import pytest
import uuid
from unittest import mock
import unittest
from src.domain.product import Product, ProductCreate
from src.services.products_services import ProductService
from src.exceptions.exceptions import ProductDoesNotExistException
from src.interfaces.product_repository import IProductRepository
def domain_products():
  product_1 = Product(
    code=str(uuid.uuid4()),
    name="Product 1",
    price=1.1,
    quantity=10
  )
  product_2 = Product(
    code=str(uuid.uuid4()),
    name="Product 2",
    price=2.2,
    quantity=20
  )
  product_3 = Product(
    code=str(uuid.uuid4()),
    name="Product 3",
    price=3.3,
    quantity=30
  )
  product_4 = Product(
    code=str(uuid.uuid4()),
    name="Product 4",
    price=4.4,
    quantity=40
  )

  return [product_1,product_2,product_3,product_4]

class ProductServiceTest(unittest.TestCase):
  def setUp(self) -> None:
    self.domain_products = domain_products()
    self.repo = mock.Mock()
    self.service = ProductService(self.repo)

  def test_product_list_without_parameters(self):
    self.repo.get_products.return_value = self.domain_products

    result = self.service.get_products()

    self.repo.get_products.assert_called_with()
    assert result == self.domain_products

  def test_service_raise_product_not_found_exception_when_product_is_not_found(self):
    code = str(uuid.uuid4())
    self.repo.get_product.side_effect = ProductDoesNotExistException(code=code)
    with pytest.raises(ProductDoesNotExistException):
      self.service.get_product(code)

  def test_should_return_product(self):
    code = str(uuid.uuid4())
    expected = Product(code=code,name="Product 1",price=1.1,quantity=10)
    self.repo.get_product.return_value = expected
    product = self.service.get_product(code)
    assert product == expected


  def test_should_create_product(self):
    product_create = ProductCreate(name="Product1", quantity=54,price=12.2)
    def create_product(product):
      return product
    self.repo.create_product = create_product
    product : Product = self.service.create_product(product_create)
    assert product.code is not None
    assert product.name == product_create.name
    assert product.quantity == product_create.quantity
    assert product.price == product_create.price
