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


class Detalle_delivery_compraDTO:
    api = Namespace(
        'detalle_delivery_compra', description='operaciones relacionadas con el detalle_delivery_compra')
    detalle_delivery_compra = api.model('detalle_delivery_compra', {
        'id_detalle_delivery': fields.Integer(required=True, description='id del detalle delivery'),
        'id_compra': fields.Integer(required=True, description='id de la compra'),
        'id_usuario': fields.Integer(required=True, description='id del usuario'),
        'direccion': fields.String(required=True, description='direccion'),
        'referencia': fields.String(required=True, description='referencia'),
        'numero_contacto': fields.String(required=True, description='numero de contacto'),
    })

###################################################################################


class EstadoDTO:
    api = Namespace(
        'estado', description='operaciones relacionadas con al estado')
    estado = api.model('estado', {
        'ID_ESTADO': fields.Integer(required=False, description='id del estado'),
        'NOMBRE': fields.String(required=True, description='nombre'),
        'DESCRIPCION': fields.String(required=True, description='descripcion'),
    })


class Modalidad_entregaDTO:
    api = Namespace(
        'modalidad_entrega', description='operaciones relacionadas con la modalidad_entrega')
    modalidad_entrega = api.model('modalidad_entrega', {
        'id_modalidad_entrega': fields.Integer(required=False, description='id de la modalidad de entrega'),
        'nombre': fields.String(required=True, description='nombre'),
        'descripcion': fields.String(required=True, description='descripcion'),
    })


class PersonaDTO:
    api = Namespace(
        'persona', description='operaciones relacionadas con la persona')
    persona = api.model('persona', {
        'id_persona': fields.Integer(required=False, description='id de la persona'),
        'usuario': fields.Integer(required=True, description='usuario'),
        'nombre': fields.String(required=True, description='nombre'),
        'apellido_paterno': fields.String(required=True, description='apellido paterno'),
        'apellido_materno': fields.String(required=True, description='apellido materno'),
        'correo': fields.String(required=True, description='correo'),
        'celular': fields.Integer(required=True, description='celular'),
        'genero': fields.Integer(required=True, description='genero'),
    })


class ProductoDTO:
    api = Namespace(
        'producto', description='operaciones relacionadas con el producto')
    producto = api.model('producto', {
        'id_producto': fields.Integer(required=False, description='id del producto'),
        'id_categoria': fields.Integer(required=True, description='id de la categoria'),
        'id_vendedor': fields.Integer(required=True, description='id del vendedor'),
        'nombre': fields.String(required=True, description='nombre'),
        'descripcion': fields.String(required=True, description='descripcion'),
        'precio': fields.Float(required=True, description='precio'),
        'imagen': fields.String(required=True, description='imagen'),
        'stock': fields.Integer(required=True, description='stock'),
        'estado_activacion': fields.Integer(required=True, description='estado de la activacion'),
        'fecha_adicion': fields.DateTime(required=True, description='fecha de la adicion'),
        'fecha_modificacion': fields.DateTime(required=True, description='fecha de la modificacion'),
    })


class RolDTO:
    api = Namespace(
        'rol', description='operaciones relacionadas con el rol')
    rol = api.model('rol', {
        'id_rol': fields.Integer(required=False, description='id del rol'),
        'nombre': fields.String(required=True, description='nombre'),
        'descripcion': fields.String(required=True, description='descripcion'),
    })


class UsuarioDTO:
    api = Namespace(
        'usuario', description='operaciones relacionadas con el usuario')
    usuario = api.model('usuario', {
        'id_usuario': fields.Integer(required=False, description='id de usuario'),
        'rol': fields.Integer(required=True, description='rol'),
        'contrasenia': fields.String(required=True, description='contrasenia'),
        'nombre_usuario': fields.String(required=True, description='nombre de usuario'),
        'id_estado_actividad': fields.Integer(required=True, description='id del estado de la actividad'),
    })


class VendedorDTO:
    api = Namespace(
        'vendedor', description='operaciones relacionadas con el vendedor')
    vendedor = api.model('vendedor', {
        'id_vendedor': fields.Integer(required=False, description='id del vendedor'),
        'paterno': fields.String(required=True, description='apellido paterno'),
        'materno': fields.String(required=True, description='apellido materno'),
        'nombre': fields.String(required=True, description='nombre'),
        'telefono': fields.String(required=True, description='telefono'),
        'dni': fields.String(required=True, description='dni'),
    })
