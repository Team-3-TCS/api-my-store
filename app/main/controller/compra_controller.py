from flask import request
from flask_restplus import Resource

from ..util.dto import CompraDTO
from ..service.compra_service import create_compra, get_compras, get_compra_id, delete_compra, update_compra

api = CompraDTO.api
_compra = CompraDTO.compra


@api.route('/')
class CompraList(Resource):
    @api.doc('list_of_registered_compras')
    @api.marshal_list_with(_compra, envelope='data')
    def get(self):
        """List all registered compras"""
        return get_compras()

    @api.response(201, 'Compra successfully created.')
    @api.doc('create a new compra')
    @api.expect(_compra, validate=True)
    def post(self):
        """Creates a new Compra """
        data = request.json
        return create_compra(data=data)


@api.route('/<id_compra>')
@api.param('id_compra', 'The compra identifier')
@api.response(404, 'Compra not found.')
class Compra(Resource):
    @api.doc('get a compra')
    @api.marshal_with(_compra)
    def get(self, id_compra):
        """get a compra given its identifier"""
        compra = get_compra_id(
            id_compra)
        if not compra:
            api.abort(404)
        else:
            return compra

    @api.doc('update a compra')
    @api.expect(_compra, validate=True)
    @api.marshal_with(_compra)
    def put(self, id_compra):
        """update a compra given its identifier"""
        data = request.json
        compra = update_compra(
            id_compra, data)
        if not compra:
            api.abort(404)
        else:
            return compra

    @api.doc('delete a compra')
    @api.marshal_with(_compra)
    def delete(self, id_compra):
        """delete a compra given its identifier"""
        compra = delete_compra(
            id_compra)
        if not compra:
            api.abort(404)
        else:
            return compra
