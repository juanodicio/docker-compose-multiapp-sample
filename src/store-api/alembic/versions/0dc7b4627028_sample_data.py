"""sample data

Revision ID: 0dc7b4627028
Revises: 28a8dccff2b0
Create Date: 2021-03-25 09:06:46.019092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dc7b4627028'
down_revision = '28a8dccff2b0'
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
