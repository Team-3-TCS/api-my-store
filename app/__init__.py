# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.cliente_controller import api as cliente_ns
from .main.controller.calificacion_producto_controller import api as calificacion_producto_ns
from .main.controller.categoria_controller import api as categoria_ns
from .main.controller.compra_controller import api as compra_ns
from .main.controller.detalle_compra_controller import api as detalle_compra_ns
from .main.controller.detalle_delivery_compra_controller import api as detalle_delivery_compra_ns
from .main.controller.estado_controller import api as estado_ns
from .main.controller.modalidad_entrega_controller import api as modalidad_entrega_ns
from .main.controller.persona_controller import api as persona_ns
from .main.controller.producto_controller import api as producto_ns
from .main.controller.rol_controller import api as rol_ns
from .main.controller.usuario_controller import api as usuario_ns
from .main.controller.vendedor_controller import api as vendedor_ns


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
api.add_namespace(detalle_delivery_compra_ns, path='/detalle_delivery_compra')
api.add_namespace(estado_ns, path='/estado')
api.add_namespace(modalidad_entrega_ns, path='/modalidad_entrega')
api.add_namespace(persona_ns, path='/persona')
api.add_namespace(producto_ns, path='/producto')
api.add_namespace(rol_ns, path='/rol')
api.add_namespace(usuario_ns, path='/usuario')
api.add_namespace(vendedor_ns, path='/vendedor')