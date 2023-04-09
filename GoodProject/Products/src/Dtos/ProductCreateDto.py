class ProductCreateDto:
  def __init__(self, name: str, price: float, quantity: int) -> None:
    self.name = name
    self.price = price
    self.quantity = quantity