"""empty message

Revision ID: 214b9dd807d6
Revises: 85e7fa4052ba
Create Date: 2021-04-23 11:59:28.537581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '214b9dd807d6'
down_revision = '85e7fa4052ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('imagen', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'imagen')
    # ### end Alembic commands ###
