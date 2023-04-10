from fastapi import APIRouter, Depends, Response, status
from src.interfaces.product_service import IProductService
from src.domain.product import Product, ProductCreate
from typing import Annotated
from ..dependencies import get_product_service
from src.exceptions.exceptions import ProductDoesNotExistException

router = APIRouter(prefix="/products")

ServiceDep = Annotated[IProductService, Depends(get_product_service)]

@router.get("/")
def product_list(service: ServiceDep)->list[Product]:
  return service.get_products()

@router.get("/{code}")
def product_get_by_code(code: str, service: ServiceDep, response: Response) -> Product|None:
  try:
    return service.get_product(code)
  except ProductDoesNotExistException:
    response.status_code = status.HTTP_404_NOT_FOUND
    return None

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(product_create : ProductCreate, service: ServiceDep)-> Product:
  return service.create_product(product_create)