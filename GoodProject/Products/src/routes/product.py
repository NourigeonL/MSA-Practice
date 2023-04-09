from fastapi import APIRouter, Depends
from src.services.products import ProductService
from src.domain.product import Product
from typing import Annotated
from ..dependencies import get_product_service

router = APIRouter()

@router.get("/products")
def product_list(service: Annotated[ProductService, Depends(get_product_service)])->list[Product]:
  return service.list_products()