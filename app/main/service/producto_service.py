from app.main import db,ma
from app.main.model.producto import Producto

class Producto_Schema(ma.Schema):
    class Meta:
        fields=('id_producto','id_categoria','id_vendedor','nombre','descripcion','precio','imagen','stock','estado_activacion','fecha_adicion','fecha_modificacion')

producto_schema=Producto_Schema()
productos_schema=Producto_Schema(many=True)

def create_producto(data):
    new_producto = Producto(
            id_producto=data['id_producto'],
            id_categoria=data['id_categoria'],
            id_vendedor=data['id_vendedor'],
            nombre=data['nombre'],
            descripcion=data['descripcion'],
            precio=data['precio'],
            imagen=data['imagen'],
            stock=data['stock'],
            estado_activacion=data['estado_activacion'],
            fecha_adicion=data['fecha_adicion'],
            fecha_modificacion=data['fecha_modificacion']
        )
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)

def get_producto():
    return Producto.query.all()


def get_producto_id(id_producto):
    producto=Producto.query.get(id_producto)
    return producto


def update_producto(id_producto,data):
    producto=Compra.query.get(nombre)
    id_categoria=data['id_categoria']
    id_vendedor=data['id_vendedor']
    nombre=data['nombre']
    descripcion=data['descripcion']
    precio=data['precio']
    imagen=data['imagen']
    stock=data['stock']
    estado_activacion=data['estado_activacion']
    fecha_adicion=data['fecha_adicion']
    fecha_modificacion=data['fecha_modificacion']
    producto.id_categoria=id_categoria
    producto.id_vendedor=id_vendedor
    producto.nombre=nombre
    producto.descripcion=descripcion
    producto.precio=precio
    producto.imagen=imagen
    producto.stock=stock
    producto.estado_activacion=estado_activacion
    producto.fecha_adicion=fecha_adicion
    producto.fecha_modificacion=fecha_modificacion
    db.session.commit()
    return producto

def delete_producto(id_producto):
    producto=Producto.query.get(id_producto)
    db.session.delete(producto)
    db.session.commit()
    return producto
