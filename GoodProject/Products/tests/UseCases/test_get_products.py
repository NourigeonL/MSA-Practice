import pytest
import unittest
from src.UseCases.GetProductsUseCase import GetProductsUseCase
from src.Entities.Product import Product
from src.Interfaces.IProductsRepository import IProductsRepository

class GetProductsTest(unittest.TestCase):
  def setUp(self) -> None:
    repo = FakeRepository()
    self.use_case = GetProductsUseCase(repo)

  def test_should_return_none_when_id_does_not_exist(self):

    product = self.use_case.get_product_by_id_use_case(0)
    assert product is None

  def test_should_return_list_products_get_all_products(self):
    products = self.use_case.get_all_products_use_case()
    assert isinstance(products, list)

  def test_should_return_one_product_when_id_exists(self):
    product = self.use_case.get_product_by_id_use_case(1)
    assert isinstance(product, Product)
    assert product.id == 1

class FakeRepository(IProductsRepository):
  def __init__(self):
    self.lst_products = [
      Product(id=1, name="My Product", quantity=50, price=2.0)
    ]

  def get_product_by_id(self, id: int):
    for product in self.lst_products:
      if product.id == id:
        return product
    return None