from conexion import *

class Modalidad_entrega(db.Model):
    Modalidad_Entrega=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    descripcion=db.Column(db.String(200))
    
    def __init__(self,Modalidad_Entrega,nombre,descripcion):
        self.Modalidad_Entrega=Modalidad_Entrega
        self.nombre=nombre
        self.descripcion=descripcion

class Modalidad_entregaSchema(ma.Schema):
    class Meta:
        fields=('Modalidad_Entrega','nombre','descripcion')

modalidad_entrega_schema=Modalidad_entregaSchema()
modalidades_entregas_schema=Modalidad_entregaSchema(many=True)

#creamos una ruta para agregar datos
@app.route('/modalidad_entrega',methods=['POST'])
def create_modalidad_entrega():
    Modalidad_Entrega=request.json['id']
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    new_modalidad_entrega=Modalidad_entrega(Modalidad_Entrega,nombre, descripcion)
    db.session.add(new_modalidad_entrega)
    db.session.commit()
    return modalidad_entrega_schema.jsonify(new_modalidad_entrega)

@app.route('/modalidad_entrega',methods=['GET'])
def get_modalidad_entrega():
    all_modalidades_entregas=Modalidad_entrega.query.all()
    result=modalidades_entregas_schema.dump(all_modalidades_entregas)
    return jsonify(result)

@app.route('/modalidad_entrega/<id_modalidad_entrega>',methods=['GET'])
def get_modalidad_entrega_id(id_modalidad_entrega):
    Modalidad_Entrega=Modalidad_entrega.query.get(id_modalidad_entrega)
    return modalidad_entrega_schema.jsonify(Modalidad_Entrega)

#actualizar datos es con el method PUT
@app.route('/modalidad_entrega/<id_modalidad_entrega>',methods=['PUT'])
def update_modalidad_entrega(id_modalidad_entrega):
    modalidad_entrega=Modalidad_entrega.query.get(id_modalidad_entrega)
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    modalidad_entrega.nombre=nombre
    modalidad_entrega.descripcion=descripcion
    db.session.commit()
    return modalidad_entrega_schema.jsonify(modalidad_entrega)

#ruta para eliminar con id, y el method DELETE
@app.route('/modalidad_entrega/<id_modalidad_entrega>',methods=['DELETE'])
def delete_modalidad_entrega(id_modalidad_entrega):
    modalidad_entrega=Modalidad_entrega.query.get(id_modalidad_entrega)
    db.session.delete(modalidad_entrega)
    db.session.commit()
    return modalidad_entrega_schema.jsonify(modalidad_entrega)