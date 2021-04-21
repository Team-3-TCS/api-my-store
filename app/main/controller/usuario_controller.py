from flask import request
from flask_restplus import Resource

from ..util.dto import UsuarioDTO
from ..service.usuario_service import *

api = UsuarioDTO.api
_usuario = UsuarioDTO.usuario


@api.route('/')
class UsuarioList(Resource):
    @api.doc('list_of_registered_usuarios')
    @api.marshal_list_with(_usuario)
    def get(self):
        """List all registered usuarios"""
        return get_usuario()

    @api.response(201, 'Usuario successfully created.')
    @api.doc('create a new usuario')
    @api.expect(_usuario, validate=True)
    def post(self):
        """Creates a new Usuario """
        data = request.json
        return create_usuario(data=data)


@api.route('/<id_usuario>')
@api.param('id_usuario', 'The usuario identifier')
@api.response(404, 'Usuario not found.')
class Usuario(Resource):
    @api.doc('get a usuario')
    @api.marshal_with(_usuario)
    def get(self, id_usuario):
        """get a usuario given its identifier"""
        usuario = get_usuario_id(id_usuario)
        if not usuario:
            api.abort(404)
        else:
            return usuario

    @api.doc('update a usuario')
    @api.expect(_usuario, validate=True)
    @api.marshal_with(_usuario)
    def put(self, id_usuario):
        """update a usuario given its identifier"""
        data = request.json
        usuario = update_usuario(id_usuario, data)
        if not usuario:
            api.abort(404)
        else:
            return usuario

    @api.doc('delete a usuario')
    @api.marshal_with(_usuario)
    def delete(self, id_usuario):
        """delete a usuario given its identifier"""
        usuario = delete_usuario(id_usuario)
        if not usuario:
            api.abort(404)
        else:
            return usuario
