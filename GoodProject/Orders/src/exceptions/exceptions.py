from src.domain.id import ID

class OrderDoesNotExistException(Exception):
  def __init__(self, *args: object, code: ID) -> None:
    self.order_code = code
    self.msg = f"The order {code.to_string()} does not exist"

class ProductDoesNotExistException(Exception):
  def __init__(self, *args: object, code: ID) -> None:
    self.product_code = code
    self.msg = f"The product {code.to_string()} does not exist"