"""empty message

Revision ID: d5e258f8df23
Revises: 8164f17a6756
Create Date: 2021-04-20 20:02:40.601841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5e258f8df23'
down_revision = '8164f17a6756'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estado',
    sa.Column('ID_ESTADO', sa.Integer(), nullable=False),
    sa.Column('NOMBRE', sa.String(length=45), nullable=True),
    sa.Column('DESCRIPCION', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('ID_ESTADO')
    )
    op.create_table('modalidad_entrega',
    sa.Column('Modalidad_Entrega', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('descripcion', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('Modalidad_Entrega')
    )
    op.create_table('persona',
    sa.Column('id_persona', sa.Integer(), nullable=False),
    sa.Column('usuario', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('apellido_paterno', sa.String(length=50), nullable=True),
    sa.Column('apellido_materno', sa.String(length=50), nullable=True),
    sa.Column('correo', sa.String(length=100), nullable=True),
    sa.Column('celular', sa.Integer(), nullable=True),
    sa.Column('genero', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_persona')
    )
    op.create_table('producto',
    sa.Column('id_producto', sa.Integer(), nullable=False),
    sa.Column('id_categoria', sa.Integer(), nullable=True),
    sa.Column('id_vendedor', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('descripcion', sa.String(length=300), nullable=True),
    sa.Column('precio', sa.Float(), nullable=True),
    sa.Column('imagen', sa.String(length=100), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('estado_activacion', sa.Integer(), nullable=True),
    sa.Column('fecha_adicion', sa.DateTime(), nullable=True),
    sa.Column('fecha_modificacion', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_producto')
    )
    op.create_table('rol',
    sa.Column('id_rol', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('descripcion', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id_rol')
    )
    op.create_table('usuario',
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('rol', sa.Integer(), nullable=True),
    sa.Column('contrasenia', sa.String(length=50), nullable=True),
    sa.Column('nombre_usuario', sa.String(length=50), nullable=True),
    sa.Column('id_estado_actividad', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_usuario')
    )
    op.create_table('vendedor',
    sa.Column('id_vendedor', sa.Integer(), nullable=False),
    sa.Column('paterno', sa.String(length=50), nullable=True),
    sa.Column('materno', sa.String(length=50), nullable=True),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('telefono', sa.String(length=10), nullable=True),
    sa.Column('dni', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id_vendedor')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vendedor')
    op.drop_table('usuario')
    op.drop_table('rol')
    op.drop_table('producto')
    op.drop_table('persona')
    op.drop_table('modalidad_entrega')
    op.drop_table('estado')
    # ### end Alembic commands ###
