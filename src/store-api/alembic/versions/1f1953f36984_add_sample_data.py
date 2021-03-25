"""Add sample data

Revision ID: 1f1953f36984
Revises: a209497c4275
Create Date: 2021-03-25 06:21:07.145399

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1f1953f36984'
down_revision = 'a209497c4275'
branch_labels = None
depends_on = None


def upgrade():
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=('products',))
    products = sa.Table('products', meta)

    rows = [
        {"name": "Hyperx Alloy Origins Core", "description": "", "brand": "HyperX", "price": 385},
        {"name": "Razer Huntsman mini", "description": "", "brand": "Razer", "price": 460},
        {"name": "Keychron K6", "description": "", "brand": "Keychron", "price": 385}
    ]
    op.bulk_insert(products, rows)


def downgrade():
    pass
