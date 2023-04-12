from .interfaces.repositories import IOrderRepository
from .services.orders_services import OrdersServices
from .repositories.memrepo import OrderMemRepo
from .interfaces.services import IOrdersServices
from typing import Annotated
from fastapi import Depends


def get_config():
  db = []
  order_repository : IOrderRepository = OrderMemRepo(db)
  order_service : IOrdersServices = OrdersServices(order_repository)
  return db, order_repository,order_service



db, order_repository, order_service = get_config()


def get_product_db():
  return db

def get_order_repository() -> IOrderRepository:
  return order_repository



def get_order_service() -> IOrdersServices:
  return order_service