"""empty message

Revision ID: dfb36bc24b6c
Revises: 9e115b4be3e3
Create Date: 2021-04-20 00:25:28.074589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfb36bc24b6c'
down_revision = '9e115b4be3e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('detalle_compra',
    sa.Column('id_detalle_compra', sa.Integer(), nullable=False),
    sa.Column('compra', sa.Integer(), nullable=True),
    sa.Column('producto', sa.Integer(), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('precio', sa.Float(), nullable=True),
    sa.Column('descuento', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id_detalle_compra')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('detalle_compra')
    # ### end Alembic commands ###
