from flask import request
from flask_restplus import Resource

from ..util.dto import VendedorDTO
from ..service.vendedor_service import *

api = VendedorDTO.api
_vendedor = VendedorDTO.vendedor


@api.route('/')
class VendedorList(Resource):
    @api.doc('list_of_registered_vendedors')
    @api.marshal_list_with(_vendedor)
    def get(self):
        """List all registered vendedors"""
        return get_vendedor()

    @api.response(201, 'Vendedor successfully created.')
    @api.doc('create a new vendedor')
    @api.expect(_vendedor, validate=True)
    def post(self):
        """Creates a new Vendedor """
        data = request.json
        return create_vendedor(data=data)


@api.route('/<id_vendedor>')
@api.param('id_vendedor', 'The vendedor identifier')
@api.response(404, 'Vendedor not found.')
class Vendedor(Resource):
    @api.doc('get a vendedor')
    @api.marshal_with(_vendedor)
    def get(self, id_vendedor):
        """get a vendedor given its identifier"""
        vendedor = get_vendedor_id(id_vendedor)
        if not vendedor:
            api.abort(404)
        else:
            return vendedor

    @api.doc('update a vendedor')
    @api.expect(_vendedor, validate=True)
    @api.marshal_with(_vendedor)
    def put(self, id_vendedor):
        """update a vendedor given its identifier"""
        data = request.json
        vendedor = update_vendedor(id_vendedor, data)
        if not vendedor:
            api.abort(404)
        else:
            return vendedor

    @api.doc('delete a vendedor')
    @api.marshal_with(_vendedor)
    def delete(self, id_vendedor):
        """delete a vendedor given its identifier"""
        vendedor = delete_vendedor(id_vendedor)
        if not vendedor:
            api.abort(404)
        else:
            return vendedor
