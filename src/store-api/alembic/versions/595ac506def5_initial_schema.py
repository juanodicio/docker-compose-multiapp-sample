"""initial schema

Revision ID: 595ac506def5
Revises: 
Create Date: 2021-03-21 23:13:32.313499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '595ac506def5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('description', sa.Unicode(250), nullable=False, default=''),
        sa.Column('price', sa.Float(12, 3), nullable=False)
    )


def downgrade():
    op.drop_table('products')
