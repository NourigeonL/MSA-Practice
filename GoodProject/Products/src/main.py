from fastapi import FastAPI
from .routes import product

app = FastAPI()

app.include_router(product.router)

# port 8001

@app.get("/")
async def root():
  return {"message":"Hello World!"}