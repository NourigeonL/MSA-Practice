from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel, NotFoundError, Migrator, Field
from starlette.requests import Request
from typing import Literal
from enum import Enum
from pydantic import BaseModel, ValidationError, validator
app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc")

redis = get_redis_connection(host="localhost", port=6379)

def must_be_positive(val: int|float) -> int|float:
    assert val >= 0, "must be a positive number"
    return val


class Product(HashModel):
    name: str
    quantity: int = 0
    price: float

    _must_be_positive_quantity = validator('quantity', allow_reuse=True)(must_be_positive)
    _must_be_positive_price = validator('price', allow_reuse=True)(must_be_positive)

    class Meta:
        database = redis

class StatusEnum(str, Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

class Order(HashModel):
    product_id: str = Field(index=True)
    quantity: int
    total: float = 0
    status: StatusEnum

    _must_be_positive_quantity = validator('quantity', allow_reuse=True)(must_be_positive)

    class Meta:
        database = redis

class OrderCreate(BaseModel):
    product_id: str
    quantity : int

Migrator().run()

@app.get("/api/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/products/")
async def get_all_products()-> list[Product]:
    return [ Product.get(pk) for pk in Product.all_pks()]

@app.get("/api/products/{product_id}/")
async def get_product_by_id(product_id: str)-> Product:
    return Product.get(product_id)

@app.get("/api/products/{product_id}/orders/")
async def get_orders_of_a_product(product_id: str)-> list[Order]:
    return Order.find(Order.product_id==product_id).all()



@app.post("/api/products/")
async def create_new_product(product: Product)-> Product:
    return product.save()

@app.delete("/api/products/{product_id}/")
async def delete_product(product_id: str)-> int:
    return Product.delete(product_id)

@app.post("/api/products/{product_id}/add-quantity/{quantity}")
async def change_product_quantity(product_id: str, quantity : int)-> Product:
    product : Product= Product.get(product_id)
    product.quantity += quantity
    return product.save()

@app.post("/api/products/{product_id}/remove-quantity/{quantity}")
async def change_product_quantity(product_id: str, quantity : int)-> Product:
    product : Product= Product.get(product_id)
    product.quantity -= quantity
    return product.save()

@app.get("/api/orders/")
async def get_all_orders()-> list[Order]:
    return [ Order.get(pk) for pk in Order.all_pks()]

@app.get("/api/orders/{order_id}/")
async def get_order_by_id(order_id: str)-> Order:
    return Order.get(order_id)

@app.post("/api/orders/")
async def create_new_order(order_create: OrderCreate) -> Order:
    product: Product = Product.get(order_create.product_id)
    if product.quantity >= order_create.quantity:
      status=StatusEnum.COMPLETED
      product.quantity -= order_create.quantity
      product.save()
    else:
      status=StatusEnum.CANCELLED
    order = Order(product_id=order_create.product_id, quantity=order_create.quantity, total=order_create.quantity*product.price, status=status)

    return order.save()

@app.delete("/api/orders/{order_id}/")
async def delete_order(order_id: str)-> int:
    return Order.delete(order_id)