from src.interfaces.product_repository import IProductRepository
from src.domain.product import Product

class MemRepo(IProductRepository):
  def __init__(self, data : list[dict[str, any]]) -> None:
    self.data = data

  def get_products(self) -> list[Product]:
    return [Product.parse_obj(product) for product in self.data]