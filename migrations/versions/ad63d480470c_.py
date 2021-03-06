"""empty message

Revision ID: ad63d480470c
Revises: 5266458f0984
Create Date: 2021-04-22 19:23:49.402813

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ad63d480470c'
down_revision = '5266458f0984'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('compra', 'id_modalidad_entrega',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'compra', 'modalidad_entrega', ['id_modalidad_entrega'], ['id_modalidad_entrega'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'compra', type_='foreignkey')
    op.alter_column('compra', 'id_modalidad_entrega',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
