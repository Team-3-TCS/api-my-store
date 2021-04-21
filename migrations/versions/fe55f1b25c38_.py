"""empty message

Revision ID: fe55f1b25c38
Revises: b47cafcdd3d1
Create Date: 2021-04-19 23:02:32.630936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe55f1b25c38'
down_revision = 'b47cafcdd3d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calificacion_producto',
    sa.Column('id_calificacion', sa.Integer(), nullable=False),
    sa.Column('id_producto', sa.Integer(), nullable=True),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.Column('puntuacion', sa.Integer(), nullable=True),
    sa.Column('comentario', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id_calificacion')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calificacion_producto')
    # ### end Alembic commands ###