from conexion import *

class Producto(db.Model):
    id_producto=db.Column(db.Integer,primary_key=True)
    id_categoria=db.Column(db.Integer)
    id_vendedor=db.Column(db.Integer)
    nombre=db.Column(db.String(100))
    descripcion=db.Column(db.String(300))
    precio=db.Column(db.Float)
    imagen=db.Column(db.String(100))
    stock=db.Column(db.Integer)
    estado_activacion=db.Column(db.Integer)
    fecha_adicion=db.Column(db.DateTime)
    fecha_modificacion=db.Column(db.DateTime)

    def __init__(self,id_producto,id_categoria,id_vendedor,nombre,descripcion,precio,imagen,stock,estado_activacion,fecha_adicion,fecha_modificacion):
        self.id_producto=id_producto
        self.id_categoria=id_categoria
        self.id_vendedor=id_vendedor
        self.Modalidad_Entrega=Modalidad_Entrega
        self.nombre=nombre
        self.descripcion=descripcion
        self.precio=precio
        self.stock=stock
        self.estado_activacion=estado_activacion
        self.fecha_adicion=fecha_adicion
        self.fecha_modificacion=fecha_modificacion


#db.create_all()

class Producto_Schema(ma.Schema):
    class Meta:
        fields=('id_producto','id_categoria','id_vendedor,nombre','descripcion','precio','imagen','stock','estado_activacion','fecha_adicion','fecha_modificacion')

producto_schema=Producto_Schema()
productos_schema=Producto_Schema(many=True)


#creamos una ruta para agregar datos
@app.route('/producto',methods=['POST'])
def create_producto():
    id_producto=request.json['id_producto']
    id_categoria=request.json['id_categoria']
    id_vendedor=request.json['id_vendedor']
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    precio=request.json['precio']
    imagen=request.json['imagen']
    stock=request.json['stock']
    estado_activacion=request.json['estado_activacion']
    fecha_adicion=request.json['fecha_adicion']
    fecha_modificacion=request.json['fecha_modificacion']
    new_producto=Producto(id_producto,id_categoria,id_vendedor,nombre,descripcion,precio,imagen,stock,estado_activacion,fecha_adicion,fecha_modificacion)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)



@app.route('/producto',methods=['GET'])
def get_producto():
    all_productos=Producto.query.all()
    result=productos_schema.dump(all_productos)
    return jsonify(result)

@app.route('/producto/<id_producto>',methods=['GET'])
def get_producto_id(id_producto):
    producto=Producto.query.get(id_producto)
    return producto_schema.jsonify(producto)

@app.route('/producto/<nombre>',methods=['GET'])
def get_producto_nombre(nombre):
    producto=Producto.query.get(nombre)
    return producto_schema.jsonify(producto)

#actualizar datos es con el method PUT
@app.route('/producto/<nombre>',methods=['PUT'])
def update_producto(id_producto):
    producto=Compra.query.get(nombre)
    id_categoria=request.json['nombre']
    id_vendedor=request.json['id_vendedor']
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    precio=request.json['precio']
    imagen=request.json['imagen']
    stock=request.json['stock']
    estado_activacion=request.json['estado_activacion']
    fecha_adicion=request.json['fecha_adicion']
    fecha_modificacion=request.json['fecha_modificacion']
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
    return producto_schema.jsonify(producto)
    return jsonify({'message':'Datos modificados'})

    #ruta para eliminar con id, y el method DELETE
@app.route('/producto/<id_producto>',methods=['DELETE'])
def delete_producto(id_producto):
    producto=Producto.query.get(id_producto)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)
    return jsonify({'message':'datos eliminados'})
