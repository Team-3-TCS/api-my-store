from flask_restplus import Namespace, fields


class ClienteDTO:
    api = Namespace(
        'cliente', description='operaciones relacionadas con el cliente')
    cliente = api.model('cliente', {
        'id_cliente': fields.Integer(required=True, description='id del cliente'),
    })


class Calificacion_productoDTO:
    api = Namespace(
        'calificacion_producto', description='operaciones relacionadas con la calificacion_producto')
    calificacion_producto = api.model('calificacion_producto', {
        'id_calificacion': fields.Integer(required=False, description='id de la calificacion_producto'),
        'id_producto': fields.Integer(required=True, description='id del producto'),
        'id_cliente': fields.Integer(required=True, description='id del cliente'),
        'puntuacion': fields.Integer(required=True, description='puntuacion de la calificacion_producto'),
        'comentario': fields.String(required=True, description='comentario de la calificacion_producto'),
    })


class CategoriaDTO:
    api = Namespace(
        'categoria', description='operaciones relacionadas con la categoria')
    categoria = api.model('categoria', {
        'id_categoria': fields.Integer(required=False, description='id de la categoria'),
        'nombre': fields.String(required=True, description='id de la categoria'),
        'descripcion': fields.String(required=True, description='id de la categoria'),
    })


class CompraDTO:
    api = Namespace(
        'compra', description='operaciones relacionadas con la compra')
    compra = api.model('compra', {
        'id_compra': fields.Integer(required=False, description='id de la compra'),
        'id_cliente': fields.Integer(required=True, description='id del cliente'),
        'id_vendedor': fields.Integer(required=True, description='id del vendedor'),
        'fecha': fields.DateTime(required=True, description='fecha de la venta'),
        'id_Estado_compra': fields.Integer(required=True, description='id del estado de la compra'),
        'id_Estado_pago': fields.Integer(required=True, description='id del estado del pago'),
        'id_modalidad_entrega': fields.Integer(required=True, description='id de l amodalidad de la entrega'),
        'descuento': fields.Float(required=True, description='descuento en la compra'),
        'id_estado': fields.Integer(required=True, description='id del estado ??'),
    })


class Detalle_compraDTO:
    api = Namespace(
        'detalle_compra', description='operaciones relacionadas con la detalle_compra')
    detalle_compra = api.model('detalle_compra', {
        'id_detalle_compra': fields.Integer(required=False, description='id de la detalle_compra'),
        'compra': fields.Integer(required=True, description='id de la compra'),
        'producto': fields.Integer(required=True, description='id del producto'),
        'cantidad': fields.Integer(required=True, description='cantidad de productos'),
        'precio': fields.Float(required=True, description='precio de la compra'),
        'descuento': fields.Float(required=True, description='descuento de la compra'),
    })
