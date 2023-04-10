from fastapi import FastAPI
from .routing.product import router as product_router

app = FastAPI()

app.include_router(product_router)

# port 8001

@app.get("/")
async def root():
  return {"message":"Hello World!"}