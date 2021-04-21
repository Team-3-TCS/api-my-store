from app.main import db
from app.main.model.detalle_compra import Detalle_compra


def create_detalle_compra(data):

    new_detalle_compra = Detalle_compra(
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


def get_detalle_compras():
    return Detalle_compra.query.all()


def get_detalle_compra_id(id_detalle_compra):
    return Detalle_compra.query.filter_by(id_detalle_compra=id_detalle_compra).first()


def update_detalle_compra(id_detalle_compra, put_detalle_compra):
    detalle_compra = Detalle_compra.query.filter_by(
        id_detalle_compra=id_detalle_compra).first()
    detalle_compra.compra = put_detalle_compra['compra']
    detalle_compra.producto = put_detalle_compra['producto']
    detalle_compra.cantidad = put_detalle_compra['cantidad']
    detalle_compra.precio = put_detalle_compra['precio']
    detalle_compra.descuento = put_detalle_compra['descuento']
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
