from flask import request
from flask_restplus import Resource

from ..util.dto import RolDTO
from ..service.rol_service import *

api = RolDTO.api
_rol = RolDTO.rol


@api.route('/')
class RolList(Resource):
    @api.doc('list_of_registered_rols')
    @api.marshal_list_with(_rol, envelope='data')
    def get(self):
        """List all registered rols"""
        return get_rol()

    @api.response(201, 'Rol successfully created.')
    @api.doc('create a new rol')
    @api.expect(_rol, validate=True)
    def post(self):
        """Creates a new Rol """
        data = request.json
        return create_rol(data=data)


@api.route('/<id_rol>')
@api.param('id_rol', 'The rol identifier')
@api.response(404, 'Rol not found.')
class Rol(Resource):
    @api.doc('get a rol')
    @api.marshal_with(_rol)
    def get(self, id_rol):
        """get a rol given its identifier"""
        rol = get_rol_id(id_rol)
        if not rol:
            api.abort(404)
        else:
            return rol

    @api.doc('update a rol')
    @api.expect(_rol, validate=True)
    @api.marshal_with(_rol)
    def put(self, id_rol):
        """update a rol given its identifier"""
        data = request.json
        rol = update_rol(id_rol, data)
        if not rol:
            api.abort(404)
        else:
            return rol

    @api.doc('delete a rol')
    @api.marshal_with(_rol)
    def delete(self, id_rol):
        """delete a rol given its identifier"""
        rol = delete_rol(id_rol)
        if not rol:
            api.abort(404)
        else:
            return rol
