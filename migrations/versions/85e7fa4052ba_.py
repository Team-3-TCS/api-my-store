"""empty message

Revision ID: 85e7fa4052ba
Revises: f108d5517411
Create Date: 2021-04-22 19:53:34.788747

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '85e7fa4052ba'
down_revision = 'f108d5517411'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('calificacion_producto', 'id_cliente',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('calificacion_producto', 'id_producto',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'calificacion_producto', 'cliente', ['id_cliente'], ['id_cliente'])
    op.create_foreign_key(None, 'calificacion_producto', 'producto', ['id_producto'], ['id_producto'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'calificacion_producto', type_='foreignkey')
    op.drop_constraint(None, 'calificacion_producto', type_='foreignkey')
    op.alter_column('calificacion_producto', 'id_producto',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('calificacion_producto', 'id_cliente',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###