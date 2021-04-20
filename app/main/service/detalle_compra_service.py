from app.main import db
from app.main.model.detalle_compra import Detalle_compra


def create_detalle_compra(data):
    detalle_compra = Detalle_compra.query.filter_by(
        id_detalle_compra=data['id_detalle_compra']
    )
    if not detalle_compra:
        new_detalle_compra = Detalle_compra(
            id_detalle_compra=data['id_detalle_compra'],
            compra=data['compra'],
            producto=data['producto'],
            cantidad=data['cantidad'],
            precio=data['precio'],
            descuento=data['descuento'],
        )
        save_changes(new_detalle_compra)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Detalle_compra already exists.',
        }
        return response_object, 409


def get_detalle_compras():
    return Detalle_compra.query.all()


def get_detalle_compra_id(id_detalle_compra):
    return Detalle_compra.query.filter_by(id_detalle_compra=id_detalle_compra).first()


def update_detalle_compra(id_detalle_compra, put_detalle_compra):
    # detalle_compra = Detalle_compra.query.get(id_detalle_compra)
    # detalle_compra = Detalle_compra.query.filter_by(
    #     id_detalle_compra=id_detalle_compra).first().update(put_detalle_compra)
    detalle_compra = Detalle_compra.query.filter(
        Detalle_compra.id_detalle_compra == str(id_detalle_compra)).first()
    detalle_compra = put_detalle_compra
    db.session.update(detalle_compra)
    db.session.commit()
    return detalle_compra


def delete_detalle_compra(id_detalle_compra):
    detalle_compra = Detalle_compra.query.get(id_detalle_compra)
    db.session.delete(detalle_compra)
    db.session.commit()
    return detalle_compra


def save_changes(data):
    db.session.add(data)
    db.session.commit()
