"""Add brand column

Revision ID: a209497c4275
Revises: 595ac506def5
Create Date: 2021-03-25 05:41:39.383297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a209497c4275'
down_revision = '595ac506def5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("products", sa.Column("brand", sa.String(100), nullable=False))


def downgrade():
    op.drop_column("products", "brand")
