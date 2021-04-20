from flask import request
from flask_restplus import Resource

from ..util.dto import Calificacion_productoDTO
from ..service.calificacion_producto_service import create_calificacion_producto, get_calificacion_productos, get_calificacion_producto_id, delete_calificacion_producto, update_calificacion_producto

api = Calificacion_productoDTO.api
_calificacion_producto = Calificacion_productoDTO.calificacion_producto


@api.route('/')
class Calificacion_productoList(Resource):
    @api.doc('list_of_registered_calificacion_productos')
    @api.marshal_list_with(_calificacion_producto, envelope='data')
    def get(self):
        """List all registered calificacion_productos"""
        return get_calificacion_productos()

    @api.response(201, 'Calificacion_producto successfully created.')
    @api.doc('create a new calificacion_producto')
    @api.expect(_calificacion_producto, validate=True)
    def post(self):
        """Creates a new Calificacion_producto """
        data = request.json
        return create_calificacion_producto(data=data)


@api.route('/<id_calificacion_producto>')
@api.param('id_calificacion_producto', 'The calificacion_producto identifier')
@api.response(404, 'Calificacion_producto not found.')
class Calificacion_producto(Resource):
    @api.doc('get a calificacion_producto')
    @api.marshal_with(_calificacion_producto)
    def get(self, id_calificacion_producto):
        """get a calificacion_producto given its identifier"""
        calificacion_producto = get_calificacion_producto_id(
            id_calificacion_producto)
        if not calificacion_producto:
            api.abort(404)
        else:
            return calificacion_producto

    @api.doc('update a calificacion_producto')
    @api.expect(_calificacion_producto, validate=True)
    @api.marshal_with(_calificacion_producto)
    def put(self, id_calificacion_producto):
        """update a calificacion_producto given its identifier"""
        data = request.json
        calificacion_producto = update_calificacion_producto(
            id_calificacion_producto, data)
        if not calificacion_producto:
            api.abort(404)
        else:
            return calificacion_producto

    @api.doc('delete a calificacion_producto')
    @api.marshal_with(_calificacion_producto)
    def delete(self, id_calificacion_producto):
        """delete a calificacion_producto given its identifier"""
        calificacion_producto = delete_calificacion_producto(
            id_calificacion_producto)
        if not calificacion_producto:
            api.abort(404)
        else:
            return calificacion_producto
