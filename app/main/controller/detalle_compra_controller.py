from flask import request
from flask_restplus import Resource

from ..util.dto import Detalle_compraDTO
from ..service.detalle_compra_service import create_detalle_compra, get_detalle_compras, get_detalle_compra_id, delete_detalle_compra, update_detalle_compra

api = Detalle_compraDTO.api
_detalle_compra = Detalle_compraDTO.detalle_compra


@api.route('/')
class CompraList(Resource):
    @api.doc('list_of_registered_detalle_compras')
    @api.marshal_list_with(_detalle_compra)
    def get(self):
        """List all registered detalle_compras"""
        return get_detalle_compras()

    @api.response(201, 'Compra successfully created.')
    @api.doc('create a new detalle_compra')
    @api.expect(_detalle_compra, validate=True)
    def post(self):
        """Creates a new Compra """
        data = request.json
        return create_detalle_compra(data=data)


@api.route('/<id_detalle_compra>')
@api.param('id_detalle_compra', 'The detalle_compra identifier')
@api.response(404, 'Compra not found.')
class Compra(Resource):
    @api.doc('get a detalle_compra')
    @api.marshal_with(_detalle_compra)
    def get(self, id_detalle_compra):
        """get a detalle_compra given its identifier"""
        detalle_compra = get_detalle_compra_id(
            id_detalle_compra)
        if not detalle_compra:
            api.abort(404)
        else:
            return detalle_compra

    @api.doc('update a detalle_compra')
    @api.expect(_detalle_compra, validate=True)
    @api.marshal_with(_detalle_compra)
    def put(self, id_detalle_compra):
        """update a detalle_compra given its identifier"""
        data = request.json
        detalle_compra = update_detalle_compra(
            id_detalle_compra, data)
        if not detalle_compra:
            api.abort(404)
        else:
            return detalle_compra

    @api.doc('delete a detalle_compra')
    @api.marshal_with(_detalle_compra)
    def delete(self, id_detalle_compra):
        """delete a detalle_compra given its identifier"""
        detalle_compra = delete_detalle_compra(
            id_detalle_compra)
        if not detalle_compra:
            api.abort(404)
        else:
            return detalle_compra
