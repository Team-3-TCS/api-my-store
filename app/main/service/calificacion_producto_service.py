from app.main import db
from app.main.model.calificacion_producto import Calificacion_producto


def create_calificacion_producto(data):

    calificacion_producto = Calificacion_producto.query.filter_by(
        id_calificacion=data['id_calificacion'])
    if not calificacion_producto:
        new_calificacion_producto = Calificacion_producto(
            id_calificacion=data['id_calificacion'],
            id_producto=data['id_producto'],
            id_calificacion_producto=data['id_calificacion_producto'],
            puntuacion=data['puntuacion'],
            comentario=data['comentario']
        )
        save_changes(new_calificacion_producto)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'calificacion producto already exists.',
        }
        return response_object, 409


def get_calificacion_productos():
    return Calificacion_producto.query.all()


def get_calificacion_producto_id(id_calificacion):
    return Calificacion_producto.query.filter_by(id_calificacion=id_calificacion).first()


def update_calificacion_producto(id_calificacion, put_calificacion_producto):
    calificacion_producto = Calificacion_producto.query.filter(
        Calificacion_producto.id_calificacion == str(id_calificacion)).first()
    calificacion_producto = put_calificacion_producto
    db.session.update(calificacion_producto)
    db.session.commit()
    return calificacion_producto


def delete_calificacion_producto(id_calificacion_producto):
    calificacion_producto = Calificacion_producto.query.get(
        id_calificacion_producto)
    db.session.delete(calificacion_producto)
    db.session.commit()
    return calificacion_producto


def save_changes(data):
    db.session.add(data)
    db.session.commit()
