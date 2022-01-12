"""add user table

Revision ID: 8036608cf58a
Revises: ba80b000eb39
Create Date: 2022-01-12 13:31:25.658561

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String


# revision identifiers, used by Alembic.
revision = '8036608cf58a'
down_revision = 'ba80b000eb39'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
