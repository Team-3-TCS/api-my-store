from flask import request
from flask_restplus import Resource

from ..util.dto import Modalidad_entregaDTO
from ..service.modalidad_entrega_service import *

api = Modalidad_entregaDTO.api
_modalidad_entrega = Modalidad_entregaDTO.modalidad_entrega


@api.route('/')
class Modalidad_entregaList(Resource):
    @api.doc('list_of_registered_modalidad_entregas')
    @api.marshal_list_with(_modalidad_entrega)
    def get(self):
        """List all registered modalidad_entregas"""
        return get_modalidad_entrega()

    @api.response(201, 'Modalidad_entrega successfully created.')
    @api.doc('create a new modalidad_entrega')
    @api.expect(_modalidad_entrega, validate=True)
    def post(self):
        """Creates a new Modalidad_entrega """
        data = request.json
        return create_modalidad_entrega(data=data)


@api.route('/<id_modalidad_entrega>')
@api.param('id_modalidad_entrega', 'The modalidad_entrega identifier')
@api.response(404, 'Modalidad_entrega not found.')
class Modalidad_entrega(Resource):
    @api.doc('get a modalidad_entrega')
    @api.marshal_with(_modalidad_entrega)
    def get(self, id_modalidad_entrega):
        """get a modalidad_entrega given its identifier"""
        modalidad_entrega = get_modalidad_entrega_id(id_modalidad_entrega)
        if not modalidad_entrega:
            api.abort(404)
        else:
            return modalidad_entrega

    @api.doc('update a modalidad_entrega')
    @api.expect(_modalidad_entrega, validate=True)
    @api.marshal_with(_modalidad_entrega)
    def put(self, id_modalidad_entrega):
        """update a modalidad_entrega given its identifier"""
        data = request.json
        modalidad_entrega = update_modalidad_entrega(id_modalidad_entrega, data)
        if not modalidad_entrega:
            api.abort(404)
        else:
            return modalidad_entrega

    @api.doc('delete a modalidad_entrega')
    @api.marshal_with(_modalidad_entrega)
    def delete(self, id_modalidad_entrega):
        """delete a modalidad_entrega given its identifier"""
        modalidad_entrega = delete_modalidad_entrega(id_modalidad_entrega)
        if not modalidad_entrega:
            api.abort(404)
        else:
            return modalidad_entrega
