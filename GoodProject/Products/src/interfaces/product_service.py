import abc
from src.domain.product import Product

class IProductService(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def get_products(self) -> list[Product]:
    raise NotImplementedError

  @abc.abstractmethod
  def get_product(self) -> Product:
    raise NotImplementedError