from fastapi import APIRouter, Depends, Response, status
from typing import Annotated
from ..dependencies import get_order_service
from src.interfaces.services import IOrdersServices

router = APIRouter(prefix="/")

ServiceDep = Annotated[IOrdersServices, Depends(get_order_service)]