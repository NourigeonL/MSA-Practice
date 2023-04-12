from src.interfaces.product_repository import IProductRepository
from src.domain.product import Product, ProductCreate
import uuid
from src.exceptions.exceptions import ProductDoesNotExistException
class MemRepo(IProductRepository):
  def __init__(self, data : list[Product]) -> None:
    self.data = data

  def get_products(self) -> list[Product]:
    return self.data

  def get_product(self, code: str) -> Product:
    for product in self.get_products():
      if product.code == code:
        return product
    raise ProductDoesNotExistException(code=code)

  def create_product(self, product: Product) -> Product:
    self.data.append(product)
    return product