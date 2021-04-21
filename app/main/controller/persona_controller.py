from flask import request
from flask_restplus import Resource

from ..util.dto import PersonaDTO
from ..service.persona_service import *

api = PersonaDTO.api
_persona = PersonaDTO.persona


@api.route('/')
class PersonaList(Resource):
    @api.doc('list_of_registered_personas')
    @api.marshal_list_with(_persona)
    def get(self):
        """List all registered personas"""
        return get_persona()

    @api.response(201, 'Persona successfully created.')
    @api.doc('create a new persona')
    @api.expect(_persona, validate=True)
    def post(self):
        """Creates a new Persona """
        data = request.json
        return create_persona(data=data)


@api.route('/<id_persona>')
@api.param('id_persona', 'The persona identifier')
@api.response(404, 'Persona not found.')
class Persona(Resource):
    @api.doc('get a persona')
    @api.marshal_with(_persona)
    def get(self, id_persona):
        """get a persona given its identifier"""
        persona = get_persona_id(id_persona)
        if not persona:
            api.abort(404)
        else:
            return persona

    @api.doc('update a persona')
    @api.expect(_persona, validate=True)
    @api.marshal_with(_persona)
    def put(self, id_persona):
        """update a persona given its identifier"""
        data = request.json
        persona = update_persona(id_persona, data)
        if not persona:
            api.abort(404)
        else:
            return persona

    @api.doc('delete a persona')
    @api.marshal_with(_persona)
    def delete(self, id_persona):
        """delete a persona given its identifier"""
        persona = delete_persona(id_persona)
        if not persona:
            api.abort(404)
        else:
            return persona
