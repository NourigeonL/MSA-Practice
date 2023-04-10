import abc
from src.domain.product import Product, ProductCreate
class IProductRepository(metaclass=abc.ABCMeta):

#   @abc.abstractmethod
#   def get(self, id: uuid.UUID) -> Product| None:
#         raise NotImplementedError

  @abc.abstractmethod
  def get_products(self) -> list[Product]:
        raise NotImplementedError

  @abc.abstractmethod
  def get_product(self, code: str) -> Product:
        raise NotImplementedError

  @abc.abstractmethod
  def create_product(self, product : Product) -> Product:
        raise NotImplementedError
