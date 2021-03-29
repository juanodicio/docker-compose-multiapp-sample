from .database import Base
import sqlalchemy as sa


class Product(Base):
    __tablename__ = "products"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(200), nullable=False)
    brand = sa.Column(sa.String(100), nullable=False, default="")
    description = sa.Column(sa.Unicode(250), nullable=False, default='')
    price = sa.Column(sa.Float(12, 3), nullable=False)
