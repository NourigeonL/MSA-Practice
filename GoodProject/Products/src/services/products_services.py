from src.interfaces.product_repository import IProductRepository
from src.interfaces.product_service import IProductService
from src.domain.product import Product, ProductCreate
import uuid
class ProductService(IProductService):
  def __init__(self, repo: IProductRepository) -> None:
    self._repo = repo

  def get_products(self) -> list[Product]:
    return self._repo.get_products()

  def get_product(self, code: str) -> Product | None:
    return self._repo.get_product(code)

  def create_product(self, product_create : ProductCreate) -> Product:
    product_dict = product_create.dict()
    product_dict["code"] = str(uuid.uuid4())
    product = Product.parse_obj(product_dict)
    return self._repo.create_product(product)

  def decrease_product_quantity(self, code: str, quantity_to_decrease: int) -> int:
    try:
      product = self.get_product(code)
      if quantity_to_decrease > product.quantity:
        return 0
      product.quantity -= quantity_to_decrease
      return quantity_to_decrease
    except Exception:
      return 0