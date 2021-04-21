from flask import request
from flask_restplus import Resource

from ..util.dto import ProductoDTO
from ..service.producto_service import *

api = ProductoDTO.api
_producto = ProductoDTO.producto


@api.route('/')
class ProductoList(Resource):
    @api.doc('list_of_registered_productos')
    @api.marshal_list_with(_producto)
    def get(self):
        """List all registered productos"""
        return get_producto()

    @api.response(201, 'Producto successfully created.')
    @api.doc('create a new producto')
    @api.expect(_producto, validate=True)
    def post(self):
        """Creates a new Producto """
        data = request.json
        return create_producto(data=data)


@api.route('/<id_producto>')
@api.param('id_producto', 'The producto identifier')
@api.response(404, 'Producto not found.')
class Producto(Resource):
    @api.doc('get a producto')
    @api.marshal_with(_producto)
    def get(self, id_producto):
        """get a producto given its identifier"""
        producto = get_producto_id(id_producto)
        if not producto:
            api.abort(404)
        else:
            return producto

    @api.doc('update a producto')
    @api.expect(_producto, validate=True)
    @api.marshal_with(_producto)
    def put(self, id_producto):
        """update a producto given its identifier"""
        data = request.json
        producto = update_producto(id_producto, data)
        if not producto:
            api.abort(404)
        else:
            return producto

    @api.doc('delete a producto')
    @api.marshal_with(_producto)
    def delete(self, id_producto):
        """delete a producto given its identifier"""
        producto = delete_producto(id_producto)
        if not producto:
            api.abort(404)
        else:
            return producto
