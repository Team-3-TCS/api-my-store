from flask import request
from flask_restplus import Resource

from ..util.dto import ClienteDTO
from ..service.cliente_service import create_cliente, get_clientes, get_cliente_id, delete_cliente, update_cliente

api = ClienteDTO.api
_cliente = ClienteDTO.cliente


@api.route('/')
class ClienteList(Resource):
    @api.doc('list_of_registered_clientes')
    @api.marshal_list_with(_cliente)
    def get(self):
        """List all registered clientes"""
        return get_clientes()

    @api.response(201, 'Cliente successfully created.')
    @api.doc('create a new cliente')
    @api.expect(_cliente, validate=True)
    def post(self):
        """Creates a new Cliente """
        data = request.json
        return create_cliente(data=data)


@api.route('/<id_cliente>')
@api.param('id_cliente', 'The cliente identifier')
@api.response(404, 'Cliente not found.')
class Cliente(Resource):
    @api.doc('get a cliente')
    @api.marshal_with(_cliente)
    def get(self, id_cliente):
        """get a cliente given its identifier"""
        cliente = get_cliente_id(id_cliente)
        if not cliente:
            api.abort(404)
        else:
            return cliente

    @api.doc('update a cliente')
    @api.expect(_cliente, validate=True)
    @api.marshal_with(_cliente)
    def put(self, id_cliente):
        """update a cliente given its identifier"""
        data = request.json
        cliente = update_cliente(id_cliente, data)
        if not cliente:
            api.abort(404)
        else:
            return cliente

    @api.doc('delete a cliente')
    @api.marshal_with(_cliente)
    def delete(self, id_cliente):
        """delete a cliente given its identifier"""
        cliente = delete_cliente(id_cliente)
        if not cliente:
            api.abort(404)
        else:
            return cliente
