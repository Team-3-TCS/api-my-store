from app.main import db
from app.main.model.categoria import Categoria


def create_categoria(data):
    new_categoria = Categoria(
        nombre=data['nombre'],
        descripcion=data['descripcion'])
    save_changes(new_categoria)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201


def get_categorias():
    return Categoria.query.all()


def get_categoria_id(id_categoria):
    return Categoria.query.filter_by(id_categoria=id_categoria).first()


def update_categoria(id_categoria, put_categoria):
    categoria = Categoria.query.filter_by(id_categoria=id_categoria).first()
    categoria.nombre = put_categoria['nombre']
    categoria.descripcion = put_categoria['descripcion']
    db.session.commit()
    return categoria


def delete_categoria(id_categoria):
    categoria = Categoria.query.get(id_categoria)
    db.session.delete(categoria)
    db.session.commit()
    return categoria


def save_changes(data):
    db.session.add(data)
    db.session.commit()
