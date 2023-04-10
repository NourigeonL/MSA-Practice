class ProductDoesNotExistException(Exception):
  def __init__(self, *args: object, code: str) -> None:
    product_code = code
    msg = "This product does not exist"