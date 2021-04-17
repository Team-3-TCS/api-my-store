from conexion import *
class Compra(db.Model):
    id_compra=db.Column(db.Integer,primary_key=True)
    id_cliente=db.Column(db.Integer)
    id_vendedor=db.Column(db.Integer)
    fecha=db.Column(db.DateTime)
    id_Estado_compra=db.Column(db.Integer)
    id_Estado_pago=db.Column(db.Integer)
    Modalidad_entrega=db.Column(db.Integer)
    descuento=db.Column(db.Float)
    id_estado=db.Column(db.Integer)
    
    def __init__(self,id_compra,id_cliente,id_vendedor,fecha,id_Estado_compra,id_Estado_pago,Modalidad_entrega,descuento,id_estado):
        self.id_compra=id_compra
        self.id_cliente=id_cliente
        self.id_vendedor=id_vendedor
        self.fecha=fecha
        self.id_Estado_compra=id_Estado_compra
        self.id_Estado_pago=id_Estado_pago
        self.Modalidad_entrega=Modalidad_entrega
        self.descuento=descuento
        self.id_estado=id_estado

class Compra_Schema(ma.Schema):
    class Meta:
        fields=('id_compra','id_cliente','id_vendedor','fecha','id_Estado_compra','id_Estado_pago','Modalidad_entrega','descuento','id_estado')

compra_schema=Compra_Schema()
compras_schema=Compra_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/compra',methods=['POST'])
def create_compra():
    id_compra=request.json['id_compra']
    id_cliente=request.json['id_cliente']
    id_vendedor=request.json['id_vendedor']
    fecha=request.json['fecha']
    id_Estado_compra=request.json['id_Estado_compra']
    id_Estado_pago=request.json['id_Estado_pago']
    Modalidad_entrega=request.json['Modalidad_entrega']
    descuento=request.json['descuento']
    id_estado=request.json['id_estado']
    new_compra=Compra(id_compra,id_cliente,id_vendedor,fecha,id_Estado_compra,id_Estado_pago,Modalidad_entrega,descuento,id_estado)
    db.session.add(new_compra)
    db.session.commit()
    return compra_schema.jsonify(new_compra)

@app.route('/compra',methods=['GET'])
def get_compra():
    all_compras=Compra.query.all()
    result=compras_schema.dump(all_compras)
    return jsonify(result)

@app.route('/compra/<id_compra>',methods=['GET'])
def get_compra_id(id_compra):
    compra=Compra.query.get(id_compra)
    return compra_schema.jsonify(compra)

#actualizar datos es con el method PUT
@app.route('/compra/<id_compra>',methods=['PUT'])
def update_compra(id_compra):
    compra=Compra.query.get(id_compra)
    id_cliente=request.json['id_cliente']
    id_vendedor=request.json['id_vendedor']
    fecha=request.json['fecha']
    id_Estado_compra=request.json['id_Estado_compra']
    id_Estado_pago=request.json['id_Estado_pago']
    Modalidad_entrega=request.json['Modalidad_entrega']
    descuento=request.json['descuento']
    id_estado=request.json['id_estado']
    compra.id_cliente=id_cliente
    compra.id_vendedor=id_vendedor
    compra.fecha=fecha
    compra.id_Estado_compra=id_Estado_compra
    compra.id_Estado_pago=id_Estado_pago
    compra.Modalidad_entrega=Modalidad_entrega
    compra.descuento=descuento
    compra.id_estado=id_estado
    db.session.commit()
    return compra_schema.jsonify(compra)

#ruta para eliminar con id, y el method DELETE
@app.route('/compra/<id_compra>',methods=['DELETE'])
def delete_compra(id_compra):
    compra=Compra.query.get(id_compra)
    db.session.delete(compra)
    db.session.commit()
    return compra_schema.jsonify(compra)