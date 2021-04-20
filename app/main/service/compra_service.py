from app.main import db
from app.main.model.compra import Compra


def create_compra(data):
    compra = Compra.query.filter_by(
        id_compra=data['id_compra']
    )
    if not compra:
        new_compra = Compra(
            id_compra=data['id_compra'],
            id_comprae=data['id_comprae'],
            id_vendedor=data['id_vendedor'],
            fecha=data['fecha'],
            id_Estado_compra=data['id_Estado_compra'],
            id_Estado_pago=data['id_Estado_pago'],
            id_modalidad_entrega=data['id_modalidad_entrega'],
            descuento=data['descuento'],
            id_estado=data['id_estado'],
        )
        save_changes(new_compra)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Compra already exists.',
        }
        return response_object, 409


def get_compras():
    return Compra.query.all()


def get_compra_id(id_compra):
    return Compra.query.filter_by(id_compra=id_compra).first()


def update_compra(id_compra, put_compra):
    # compra = Compra.query.get(id_compra)
    # compra = Compra.query.filter_by(
    #     id_compra=id_compra).first().update(put_compra)
    compra = Compra.query.filter(
        Compra.id_compra == str(id_compra)).first()
    compra = put_compra
    db.session.update(compra)
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
