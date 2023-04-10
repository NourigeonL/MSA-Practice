from fastapi import APIRouter, Depends
from src.interfaces.product_service import IProductService
from src.domain.product import Product
from typing import Annotated
from ..dependencies import get_product_service

router = APIRouter(prefix="/products")

ServiceDep = Annotated[IProductService, Depends(get_product_service)]

@router.get("/")
def product_list(service: ServiceDep)->list[Product]:
  return service.get_products()

@router.get("/{code}")
def product_get_by_code(code: str, service: ServiceDep) -> Product:
  return service.get_product(code)