from login import *
from typing import List

class Product(BaseModel):
    name: str
    sku: str
    price: float
    url: str

products=[]

@app.get("/products", response_model=List[Product])
def list_products(current_user: Annotated[User, Depends(get_current_active_user)]):
    return products

@app.post("/products")
def create_product(
    product: Product,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    products.append(product)
    return product

