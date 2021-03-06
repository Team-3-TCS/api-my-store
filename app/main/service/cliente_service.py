from app.main import db
from app.main.model.cliente import Cliente


def create_cliente(data):

    new_cliente = Cliente(id_cliente=data['id_cliente'])
    save_changes(new_cliente)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201


def get_clientes():
    return Cliente.query.all()


def get_cliente_id(id_cliente):
    return Cliente.query.filter_by(id_cliente=id_cliente).first()


def update_cliente(id_cliente, put_client):
    cliente = Cliente.query.filter_by(id_cliente=id_cliente).first()
    cliente.id_cliente = put_client['id_cliente']
    db.session.commit()
    return cliente


def delete_cliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    db.session.delete(cliente)
    db.session.commit()
    return cliente


def save_changes(data):
    db.session.add(data)
    db.session.commit()
