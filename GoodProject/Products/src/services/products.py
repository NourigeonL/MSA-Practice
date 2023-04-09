from src.interfaces.product_repository import IProductRepository
from src.domain.product import Product

class ProductService():
  def __init__(self, repo: IProductRepository) -> None:
    self._repo = repo

  def get_products(self) -> list[Product]:
    return self._repo.get_products()