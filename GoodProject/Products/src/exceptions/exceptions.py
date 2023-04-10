class ProductDoesNotExistException(Exception):
  def __init__(self, *args: object, code: str) -> None:
    self.product_code = code
    self.msg = "This product does not exist"