from .interfaces.product_repository import IProductRepository
from .repositories.memrepo import MemRepo
from .services.products import ProductService
from .interfaces.product_service import IProductService

db = []

product_repository = MemRepo(db)

def get_product_repository() -> IProductRepository:
  return product_repository

product_service = ProductService(product_repository)

def get_product_service() -> IProductService:
  return product_service
