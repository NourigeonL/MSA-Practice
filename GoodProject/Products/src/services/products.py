from src.interfaces.product_repository import IProductRepository
from src.interfaces.product_service import IProductService
from src.domain.product import Product

class ProductService(IProductService):
  def __init__(self, repo: IProductRepository) -> None:
    self._repo = repo

  def get_products(self) -> list[Product]:
    return self._repo.get_products()

  def get_product(self) -> Product | None:
    raise NotImplementedError