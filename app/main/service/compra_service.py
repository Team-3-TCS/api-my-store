from app.main import db
from app.main.model.compra import Compra


def create_compra(data):
    new_compra = Compra(
        id_cliente=data['id_cliente'],
        id_vendedor=data['id_vendedor'],
        fecha=data['fecha'],
        id_Estado_compra=data['id_Estado_compra'],
        id_Estado_pago=data['id_Estado_pago'],
        id_modalidad_entrega=data['id_modalidad_entrega'],
        descuento=data['descuento'],
    )
    save_changes(new_compra)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201


def get_compras():
    return Compra.query.all()


def get_compra_id(id_compra):
    return Compra.query.filter_by(id_compra=id_compra).first()


def update_compra(id_compra, put_compra):
    compra = Compra.query.filter_by(id_compra=id_compra).first()
    compra.id_cliente = put_compra['id_cliente']
    compra.id_vendedor = put_compra['id_vendedor']
    compra.fecha = put_compra['fecha']
    compra.id_Estado_compra = put_compra['id_Estado_compra']
    compra.id_Estado_pago = put_compra['id_Estado_pago']
    compra.id_modalidad_entrega = put_compra['id_modalidad_entrega']
    compra.descuento = put_compra['descuento']
    db.session.commit()
    return compra


def delete_compra(id_compra):
    compra = Compra.query.get(id_compra)
    db.session.delete(compra)
    db.session.commit()
    return compra


def save_changes(data):
    db.session.add(data)
    db.session.commit()
