from flask import request
from flask_restplus import Resource

from ..util.dto import EstadoDTO
from ..service.estado_service import *

api = EstadoDTO.api
_estado = EstadoDTO.estado


@api.route('/')
class EstadoList(Resource):
    @api.doc('list_of_registered_estados')
    @api.marshal_list_with(_estado, envelope='data')
    def get(self):
        """List all registered estados"""
        return get_estado()

    @api.response(201, 'Estado successfully created.')
    @api.doc('create a new estado')
    @api.expect(_estado, validate=True)
    def post(self):
        """Creates a new Estado """
        data = request.json
        return create_estado(data=data)


@api.route('/<id_estado>')
@api.param('id_estado', 'The estado identifier')
@api.response(404, 'Estado not found.')
class Estado(Resource):
    @api.doc('get a estado')
    @api.marshal_with(_estado)
    def get(self, id_estado):
        """get a estado given its identifier"""
        estado = get_estado_id(id_estado)
        if not estado:
            api.abort(404)
        else:
            return estado

    @api.doc('update a estado')
    @api.expect(_estado, validate=True)
    @api.marshal_with(_estado)
    def put(self, id_estado):
        """update a estado given its identifier"""
        data = request.json
        estado = update_estado(id_estado, data)
        if not estado:
            api.abort(404)
        else:
            return estado

    @api.doc('delete a estado')
    @api.marshal_with(_estado)
    def delete(self, id_estado):
        """delete a estado given its identifier"""
        estado = delete_estado(id_estado)
        if not estado:
            api.abort(404)
        else:
            return estado
