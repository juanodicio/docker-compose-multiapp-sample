from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db


app = FastAPI()
app.debug = True


@app.get("api/products")
def list_products():
    return products


@app.post("api/products")
def create_product():
    pass

