from flask_restplus import Namespace, fields


class ClienteDTO:
    api = Namespace(
        'cliente', description='operaciones relacionadas con el cliente')
    cliente = api.model('cliente', {
        'id_cliente': fields.String(required=True, description='id del cliente'),
    })
