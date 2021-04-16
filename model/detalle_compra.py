from conexion import *
class Detalle_compra(db.Model):
    id_detalle_compra=db.Column(db.Integer,primary_key=True)
    compra=db.Column(db.Integer)
    producto=db.Column(db.Integer)
    cantidad=db.Column(db.Integer)
    precio=db.Column(db.Float)
    descuento=db.Column(db.Float)
    
    def __init__(self,id_detalle_compra,compra,producto,cantidad,precio,descuento):
        self.id_detalle_compra=id_detalle_compra
        self.compra=compra
        self.producto=producto
        self.cantidad=cantidad
        self.precio=precio
        self.descuento=descuento

db.create_all()

class Detalle_compra_Schema(ma.Schema):
    class Meta:
        fields=('id_detalle_compra','compra','producto','cantidad','precio','descuento')

detalle_compra_schema=Detalle_compra_Schema()
detalles_compras_schema=Detalle_compra_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/detalle_compra',methods=['POST'])
def create_detalle_compra():
    id_detalle_compra=request.json['id_detalle_compra']
    compra=request.json['compra']
    producto=request.json['producto']
    cantidad=request.json['cantidad']
    precio=request.json['precio']
    descuento=request.json['descuento']
    new_detalle_compra=Detalle_compra(id_detalle_compra,compra,producto,cantidad,precio,descuento)
    db.session.add(new_detalle_compra)
    db.session.commit()
    return detalle_compra_schema.jsonify(new_detalle_compra)

@app.route('/detalle_compra',methods=['GET'])
def get_detalle_compra():
    all_detalles_compras=Detalle_compra.query.all()
    result=detalles_compras_schema.dump(all_detalles_compras)
    return jsonify(result)

@app.route('/detalle_compra/<id_detalle_compra>',methods=['GET'])
def get_detalle_compra_id(id_detalle_compra):
    detalle_compra=Detalle_compra.query.get(id_detalle_compra)
    return detalle_compra_schema.jsonify(detalle_compra)

#actualizar datos es con el method PUT
@app.route('/detalle_compra/<id_detalle_compra>',methods=['PUT'])
def update_detalle_compra(id_detalle_compra):
    detalle_compra=Detalle_compra.query.get(id_detalle_compra)
    compra=request.json['compra']
    producto=request.json['producto']
    cantidad=request.json['cantidad']
    precio=request.json['precio']
    descuento=request.json['descuento']
    detalle_compra.compra=compra
    detalle_compra.producto=producto
    detalle_compra.cantidad=cantidad
    detalle_compra.precio=precio
    detalle_compra.descuento=descuento
    db.session.commit()
    return detalle_compra_schema.jsonify(detalle_compra)

#ruta para eliminar con id, y el method DELETE
@app.route('/detalle_compra/<id_detalle_compra>',methods=['DELETE'])
def delete_detalle_compra(id_detalle_compra):
    detalle_compra=Detalle_compra.query.get(id_detalle_compra)
    db.session.delete(detalle_compra)
    db.session.commit()
    return detalle_compra_schema.jsonify(detalle_compra)