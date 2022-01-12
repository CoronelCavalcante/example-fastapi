"""add last few columns to posts table

Revision ID: ad4a3a51891e
Revises: 660055d06f84
Create Date: 2022-01-12 14:08:30.000422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad4a3a51891e'
down_revision = '660055d06f84'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('poblished', sa.Boolean(), nullable=False, server_default='TRUE'), )
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
