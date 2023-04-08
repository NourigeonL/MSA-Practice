from src.Interfaces.IProductsRepository import IProductsRepository


class GetProductsUseCase:
  def __init__(self, repo : IProductsRepository):
    self._repo = repo

  def get_product_by_id_use_case(self, id: int):
    return self._repo.get_product_by_id(id)

  def get_all_products_use_case(self):
    return []