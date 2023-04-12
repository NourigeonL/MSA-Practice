from fastapi import APIRouter, Depends, Response, status, BackgroundTasks
from typing import Annotated, List
from ..dependencies import get_order_service
from src.interfaces.services import IOrdersServices
from src.exceptions.exceptions import OrderDoesNotExistException
from src.domain.orders import Order, OrderCreate, OrderStatus
from src.domain.id import ID
import time, requests
router = APIRouter()

ServiceDep = Annotated[IOrdersServices, Depends(get_order_service)]

@router.get("/orders/")
async def get_orders(service : ServiceDep)-> list[Order]:
  return service.get_orders()

@router.get("/orders/{code}/")
async def get_order_by_id(code : ID, service : ServiceDep, response : Response)-> Order|None:
  try:
    return service.get_order(code=code)
  except OrderDoesNotExistException:
    response.status_code = status.HTTP_404_NOT_FOUND
    return None

@router.post("/orders/", status_code=status.HTTP_201_CREATED)
async def create_order(order_create : OrderCreate, service : ServiceDep, background_tasks : BackgroundTasks):
  order = service.create_order(order_create)

  background_tasks.add_task(process_order, order, service)

  return order

@router.get("/products/{product_code}/orders")
async def get_orders_of_product(product_code: ID, service : ServiceDep, response : Response) -> list[Order]:
  return service.get_orders_of_product(product_code)

def process_order(order: Order, service : IOrdersServices):
  time.sleep(5)

  req = requests.post(f"http://localhost:8001/products/{order.product}/remove-quantity/{order.quantity}")
  quantity = req.json()
  print(quantity)
  print("starting service")
  service.verify_order(order, quantity)
  print("finished service")