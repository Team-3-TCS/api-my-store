from app.main import db
from app.main.model.categoria import Categoria


def create_categoria(data):
    categoria = Categoria.query.filter_by(id_categoria=data['id_categoria'])
    if not categoria:
        new_categoria = Categoria(id_categoria=data['id_categoria'],
                                  nombre=data['nombre'],
                                  descripcion=data['descripcion'])
        save_changes(new_categoria)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Categoria already exists.',
        }
        return response_object, 409


def get_categorias():
    return Categoria.query.all()


def get_categoria_id(id_categoria):
    return Categoria.query.filter_by(id_categoria=id_categoria).first()


def update_categoria(id_categoria, put_categoria):
    # categoria = Categoria.query.get(id_categoria)
    # categoria = Categoria.query.filter_by(
    #     id_categoria=id_categoria).first().update(put_categoria)
    categoria = Categoria.query.filter(
        Categoria.id_categoria == str(id_categoria)).first()
    categoria = put_categoria
    db.session.update(categoria)
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
