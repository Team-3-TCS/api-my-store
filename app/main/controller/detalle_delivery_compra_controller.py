from flask import request
from flask_restplus import Resource

from ..util.dto import Detalle_delivery_compraDTO
from ..service.detalle_delivery_compra_service import *

api = Detalle_delivery_compraDTO.api
_detalle_delivery_compra = Detalle_delivery_compraDTO.detalle_delivery_compra


@api.route('/')
class Detalle_delivery_compraList(Resource):
    @api.doc('list_of_registered_detalle_delivery_compras')
    @api.marshal_list_with(_detalle_delivery_compra)
    def get(self):
        """List all registered detalle_delivery_compras"""
        return get_detalle_delivery_compra()

    @api.response(201, 'Detalle_delivery_compra successfully created.')
    @api.doc('create a new detalle_delivery_compra')
    @api.expect(_detalle_delivery_compra, validate=True)
    def post(self):
        """Creates a new Detalle_delivery_compra """
        data = request.json
        return create_detalle_delivery_compra(data=data)


@api.route('/<id_detalle_delivery_compra>')
@api.param('id_detalle_delivery_compra', 'The detalle_delivery_compra identifier')
@api.response(404, 'Detalle_delivery_compra not found.')
class Detalle_delivery_compra(Resource):
    @api.doc('get a detalle_delivery_compra')
    @api.marshal_with(_detalle_delivery_compra)
    def get(self, id_detalle_delivery_compra):
        """get a detalle_delivery_compra given its identifier"""
        detalle_delivery_compra = get_detalle_delivery_compra_id(id_detalle_delivery_compra)
        if not detalle_delivery_compra:
            api.abort(404)
        else:
            return detalle_delivery_compra

    @api.doc('update a detalle_delivery_compra')
    @api.expect(_detalle_delivery_compra, validate=True)
    @api.marshal_with(_detalle_delivery_compra)
    def put(self, id_detalle_delivery_compra):
        """update a detalle_delivery_compra given its identifier"""
        data = request.json
        detalle_delivery_compra = update_detalle_delivery_compra(id_detalle_delivery_compra, data)
        if not detalle_delivery_compra:
            api.abort(404)
        else:
            return detalle_delivery_compra

    @api.doc('delete a detalle_delivery_compra')
    @api.marshal_with(_detalle_delivery_compra)
    def delete(self, id_detalle_delivery_compra):
        """delete a detalle_delivery_compra given its identifier"""
        detalle_delivery_compra = delete_detalle_delivery_compra(id_detalle_delivery_compra)
        if not detalle_delivery_compra:
            api.abort(404)
        else:
            return detalle_delivery_compra
