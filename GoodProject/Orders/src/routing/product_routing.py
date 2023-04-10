from fastapi import APIRouter, Depends, Response, status
from typing import Annotated
import src.exceptions.exceptions

router = APIRouter(prefix="/")