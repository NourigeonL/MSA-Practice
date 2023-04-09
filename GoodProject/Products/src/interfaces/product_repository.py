import abc
from src.domain.product import Product
import uuid
class IProductRepository(metaclass=abc.ABCMeta):

#   @abc.abstractmethod
#   def get(self, id: uuid.UUID) -> Product| None:
#         raise NotImplementedError

  @abc.abstractmethod
  def list(self) -> list[Product]:
        raise NotImplementedError
