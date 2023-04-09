import uuid
from src.domain.product import Product
import pytest
import unittest

class ProductTest(unittest.TestCase):

  def test_product_model_init(self):
    code = uuid.uuid4()
    product = Product(code=code, name= "Product 1", price=10.0, quantity=50)
    assert product.code == code
    assert product.quantity == 50
    assert product.price == 10.0
    assert product.name == "Product 1"

  def test_product_model_from_dict(self):
    code = uuid.uuid4()
    init_dict = {
      "code": code,
      "name": "Product 2",
      "price": 2.35,
      "quantity": 10
    }
    product = Product.parse_obj(init_dict)
    assert product.code == code
    assert product.quantity == 10
    assert product.price == 2.35
    assert product.name == "Product 2"

  def test_product_model_to_dict(self):
    init_dict = {
      "code": uuid.uuid4(),
      "name": "Product 3",
      "price": 2.35,
      "quantity": 10
    }
    product = Product.parse_obj(init_dict)

    assert product.dict() == init_dict

  def test_product_model_comparaison(self):
    init_dict = {
      "code": uuid.uuid4(),
      "name": "Product 3",
      "price": 2.35,
      "quantity": 10
    }
    product1 = Product.parse_obj(init_dict)
    product2 = Product.parse_obj(init_dict)

    assert product1 == product2