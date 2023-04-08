from fastapi import FastAPI

app = FastAPI()

# port 8001

@app.get("/")
async def root():
  return {"message":"Hello World!"}

@app.get("/products")
async def get_all_products():
  return []