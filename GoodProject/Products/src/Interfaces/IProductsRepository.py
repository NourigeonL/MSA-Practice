import abc
from src.Entities.Product import Product

class IProductsRepository(metaclass=abc.ABCMeta):
  @classmethod
  def __subclasshook__(cls, subclass):
      return (hasattr(subclass, 'get_product_by_id') and
              callable(subclass.get_product_by_id)or
              NotImplemented)

  @abc.abstractmethod
  def get_product_by_id(self, id: int) -> Product| None:
        raise NotImplementedError