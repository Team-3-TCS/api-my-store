from conexion import *

#una clase tareas, y con un parametro del modelo que viene de la base de datos, se define que se va a 
# guardar en la base de datos
class Detalle_delivery_compra(db.Model):
    id_detalle_delivery=db.Column(db.Integer,primary_key=True)
    id_compra=db.Column(db.Integer)
    id_usuario=db.Column(db.Integer)
    direccion=db.Column(db.String(100))
    referencia=db.Column(db.String(100))
    numero_contacto=db.Column(db.String(45))
    
    def __init__(self,id_detalle_delivery,id_compra,id_usuario,direccion,referencia,numero_contacto):
        self.id_detalle_delivery=id_detalle_delivery
        self.id_compra=id_compra
        self.id_usuario=id_usuario
        self.direccion=direccion
        self.referencia=referencia
        self.numero_contacto=numero_contacto

#lee toda la clase y apartir de eso crea tablas
#db.create_all()

#creamos una clase esquema, y importamos desde ma y desde ma importamos esquema
class Detalle_delivery_compra_Schema(ma.Schema):
    class Meta:
        #definimos los campos que quiero obtener cada ves que interactue con este esquema
        fields=('id_detalle_delivery','id_compra','id_usuario','direccion','referencia','numero_contacto')

detalle_delivery_compra_schema=Detalle_delivery_compra_Schema()
detalle_delivery_compras_schema=Detalle_delivery_compra_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/detalle_delivery_compra',methods=['POST'])
def create_detalle_delivery_compra():
    id_detalle_delivery=request.json['id_detalle_delivery']
    id_compra=request.json['id_compra']
    id_usuario=request.json['id_usuario']
    direccion=request.json['direccion']
    referencia=request.json['referencia']
    numero_contacto=request.json['numero_contacto']
    #creo un esquema con las variables y lo guardo en una variable new_task
    new_detalle_delivery_compra=Detalle_delivery_compra(id_detalle_delivery,id_compra,id_usuario,direccion,referencia,numero_contacto)
    db.session.add(new_detalle_delivery_compra)
    db.session.commit()
    return detalle_delivery_compra_schema.jsonify(new_detalle_delivery_compra)

@app.route('/detalle_delivery_compra',methods=['GET'])
def get_detalle_delivery_compra():
    all_detalle_delivery_compras=Detalle_delivery_compra.query.all()
    result=detalle_delivery_compras_schema.dump(all_detalle_delivery_compras)
    return jsonify(result)

@app.route('/detalle_delivery_compra/<id_detalle_delivery>',methods=['GET'])
def get_detalle_delivery_compra_id(id_detalle_delivery):
    detalle_delivery_compra=Detalle_delivery_compra.query.get(id_detalle_delivery)
    return detalle_delivery_compra_schema.jsonify(detalle_delivery_compra)

#actualizar datos es con el method PUT
@app.route('/detalle_delivery_compra/<id_detalle_delivery>',methods=['PUT'])
def update_detalle_delivery_compra(id_detalle_delivery):
    detalle_delivery_compra=Detalle_delivery_compra.query.get(id_detalle_delivery)
    id_compra=request.json['id_compra']
    id_usuario=request.json['id_usuario']
    direccion=request.json['direccion']
    referencia=request.json['referencia']
    numero_contacto=request.json['numero_contacto']
    #actualizamos con las variables que recibieron los datos
    detalle_delivery_compra.id_compra=id_compra
    detalle_delivery_compra.id_usuario=id_usuario
    detalle_delivery_compra.direccion=direccion
    detalle_delivery_compra.referencia=referencia
    detalle_delivery_compra.numero_contacto=numero_contacto
    db.session.commit()
    return detalle_delivery_compra_schema.jsonify(detalle_delivery_compra)

#ruta para eliminar con id, y el method DELETE
@app.route('/detalle_delivery_compra/<id_detalle_delivery>',methods=['DELETE'])
def delete_detalle_delivery_compra(id_detalle_delivery):
    detalle_delivery_compra=Detalle_delivery_compra.query.get(id_detalle_delivery)
    db.session.delete(detalle_delivery_compra)
    db.session.commit()
    return detalle_delivery_compra_schema.jsonify(detalle_delivery_compra)