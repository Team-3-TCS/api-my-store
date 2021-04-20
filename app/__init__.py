# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.cliente_controller import api as cliente_ns
from .main.controller.calificacion_producto_controller import api as calificacion_producto_ns
from .main.controller.categoria_controller import api as categoria_ns
from .main.controller.compra_controller import api as compra_ns
from .main.controller.detalle_compra_controller import api as detalle_compra_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='API DE MYSTORE',
          version='1.0',
          description='Una API creada para el proyecto MyStore'
          )

api.add_namespace(cliente_ns, path='/cliente')
api.add_namespace(calificacion_producto_ns, path='/calificacion_producto')
api.add_namespace(categoria_ns, path='/categoria')
api.add_namespace(compra_ns, path='/compra')
api.add_namespace(detalle_compra_ns, path='/detalle_compra')
