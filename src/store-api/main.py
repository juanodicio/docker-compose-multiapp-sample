from fastapi import FastAPI
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: float
    image_url: str


products = [
    Product(name="Hyperx Alloy Origins Core", description="", price=385, image_url=""),
    Product(name="Razer huntsman mini", description="", price=385, image_url=""),
    Product(name="Keychron K6", description="", price=385, image_url="")
]


app = FastAPI()
app.debug = True


@app.get("api/products")
def list_products():
    return products


@app.post("api/products")
def create_product():
    pass

