from flask import request
from flask_restplus import Resource

from ..util.dto import CategoriaDTO
from ..service.categoria_service import create_categoria, get_categorias, get_categoria_id, delete_categoria, update_categoria

api = CategoriaDTO.api
_categoria = CategoriaDTO.categoria


@api.route('/')
class CategoriaList(Resource):
    @api.doc('list_of_registered_categorias')
    @api.marshal_list_with(_categoria)
    def get(self):
        """List all registered categorias"""
        return get_categorias()

    @api.response(201, 'Categoria successfully created.')
    @api.doc('create a new categoria')
    @api.expect(_categoria, validate=True)
    def post(self):
        """Creates a new Categoria """
        data = request.json
        return create_categoria(data=data)


@api.route('/<id_categoria>')
@api.param('id_categoria', 'The categoria identifier')
@api.response(404, 'Categoria not found.')
class Categoria(Resource):
    @api.doc('get a categoria')
    @api.marshal_with(_categoria)
    def get(self, id_categoria):
        """get a categoria given its identifier"""
        categoria = get_categoria_id(
            id_categoria)
        if not categoria:
            api.abort(404)
        else:
            return categoria

    @api.doc('update a categoria')
    @api.expect(_categoria, validate=True)
    @api.marshal_with(_categoria)
    def put(self, id_categoria):
        """update a categoria given its identifier"""
        data = request.json
        categoria = update_categoria(
            id_categoria, data)
        if not categoria:
            api.abort(404)
        else:
            return categoria

    @api.doc('delete a categoria')
    @api.marshal_with(_categoria)
    def delete(self, id_categoria):
        """delete a categoria given its identifier"""
        categoria = delete_categoria(
            id_categoria)
        if not categoria:
            api.abort(404)
        else:
            return categoria
