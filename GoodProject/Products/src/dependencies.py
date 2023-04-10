from .interfaces.product_repository import IProductRepository
from .repositories.memrepo import MemRepo
from .services.products_services import ProductService
from .interfaces.product_service import IProductService
from typing import Annotated
from fastapi import Depends


def get_config():
  db = []
  product_repository = MemRepo(db)
  product_service = ProductService(product_repository)
  return db, product_repository,product_service



db, product_repository, product_service = get_config()


def get_product_db():
  return db

def get_product_repository() -> IProductRepository:
  return product_repository



def get_product_service() -> IProductService:
  return product_service
