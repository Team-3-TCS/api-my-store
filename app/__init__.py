# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.cliente_controller import api as cliente_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='API DE MYSTORE',
          version='1.0',
          description='Una API creada para el proyecto MyStore'
          )

api.add_namespace(cliente_ns, path='/cliente')
