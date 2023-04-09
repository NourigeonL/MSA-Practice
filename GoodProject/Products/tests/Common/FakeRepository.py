from src.interfaces.product_repository import IProductRepository, Product
import uuid
class FakeRepository(IProductRepository):
  def __init__(self, db : list[Product]):
    self.__db = db

  def get(self, code: uuid.UUID):
    for product in self.__db:
      if product.code == code:
        return product
    return None

  def list(self):
    return self.__db.copy()