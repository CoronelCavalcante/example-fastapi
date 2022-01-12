"""add content column to posts table

Revision ID: ba80b000eb39
Revises: 8d4f9caa1110
Create Date: 2022-01-12 13:23:25.852850

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = 'ba80b000eb39'
down_revision = '8d4f9caa1110'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
