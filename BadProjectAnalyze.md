# What is wrong with the architecture of this project?

Since it a very simple app, I will ignore the fact that there is only one file and no try catch (because I tried to make this project fast enough)

## No abstraction

The application is very coupled to the `redis_om` package

```python
from redis_om import get_redis_connection, HashModel
redis = get_redis_connection(host="localhost", port=6379)

class Product(HashModel):
    name: str
    quantity: int = 0
    price: float

    class Meta:
        database = redis

@app.get("/api/products/{product_id}/")
async def get_product_by_id(product_id: str)-> Product:
    return Product.get(product_id)
```

If we decide to change the ORM which has different behavior and different methods(like for example use `int` for the primary key with an auto-increment, and to retrieve a single object the method is `Product.objects.get(*args : any, **kwargs: any)`), we need to change the whole function.

The endpoint shouldn't be aware of what type of database we are using.
