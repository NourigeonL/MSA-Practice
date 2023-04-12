import abc
from src.domain.product import Product, ProductCreate

class IProductService(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def get_products(self) -> list[Product]:
    raise NotImplementedError

  @abc.abstractmethod
  def get_product(self, code: str) -> Product:
    raise NotImplementedError

  @abc.abstractmethod
  def create_product(self, product_create : ProductCreate) -> Product:
    raise NotImplementedError

  @abc.abstractmethod
  def decrease_product_quantity(self, code: str, quantity_to_decrease: int) -> int:
    raise NotImplementedError
