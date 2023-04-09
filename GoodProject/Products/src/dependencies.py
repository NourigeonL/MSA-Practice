from .interfaces.product_repository import IProductRepository
from .repository.memrepo import MemRepo
from typing import Annotated, AsyncGenerator
from fastapi import Depends
from contextlib import asynccontextmanager
from .services.products import ProductService

db = []

product_repository = MemRepo(db)

def get_product_repository() -> IProductRepository:
  return product_repository

product_service = ProductService(product_repository)

def get_product_service() -> ProductService:
  return product_service
