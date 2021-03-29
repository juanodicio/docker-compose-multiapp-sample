from typing import List
from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import uvicorn
import os

env_file = '.env'
if os.environ.get("APP_ENV"):
    env_file = '.env.' + os.environ['APP_ENV']

load_dotenv(env_file)

from store.database import SessionLocal, engine
from store import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/products", response_model=List[schemas.Product])
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=5000, reload=True)
