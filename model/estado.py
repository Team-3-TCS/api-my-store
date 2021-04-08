from conexion import *
class Estado(db.Model):
    ID_ESTADO=db.Column(db.Integer,primary_key=True)
    NOMBRE=db.Column(db.String(45))
    DESCRIPCION=db.Column(db.String(200))
    
    def __init__(self,ID_ESTADO,NOMBRE,DESCRIPCION):
        self.ID_ESTADO=ID_ESTADO
        self.NOMBRE=NOMBRE
        self.DESCRIPCION=DESCRIPCION

db.create_all()

class Estado_Schema(ma.Schema):
    class Meta:
        fields=('ID_ESTADO','NOMBRE','DESCRIPCION')

estado_schema=Estado_Schema()
estados_schema=Estado_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/estado',methods=['POST'])
def create_estado():
    ID_ESTADO=request.json['ID_ESTADO']
    NOMBRE=request.json['NOMBRE']
    DESCRIPCION=request.json['DESCRIPCION']
    new_estado=Estado(ID_ESTADO,NOMBRE,DESCRIPCION)
    db.session.add(new_estado)
    db.session.commit()
    return estado_schema.jsonify(new_estado)

@app.route('/estado',methods=['GET'])
def get_estado():
    all_estados=Estado.query.all()
    result=estados_schema.dump(all_estados)
    return jsonify(result)

@app.route('/estado/<ID_ESTADO>',methods=['GET'])
def get_estado_id(ID_ESTADO):
    estado=Estado.query.get(ID_ESTADO)
    return estado_schema.jsonify(estado)

#actualizar datos es con el method PUT
@app.route('/estado/<ID_ESTADO>',methods=['PUT'])
def update_estado(ID_ESTADO):
    estado=Estado.query.get(ID_ESTADO)
    NOMBRE=request.json['NOMBRE']
    DESCRIPCION=request.json['DESCRIPCION']
    estado.NOMBRE=NOMBRE
    estado.DESCRIPCION=DESCRIPCION
    db.session.commit()
    return estado_schema.jsonify(estado)

#ruta para eliminar con id, y el method DELETE
@app.route('/estado/<ID_ESTADO>',methods=['DELETE'])
def delete_estado(ID_ESTADO):
    estado=Estado.query.get(ID_ESTADO)
    db.session.delete(estado)
    db.session.commit()
    return estado_schema.jsonify(estado)

#creamos una ruta principal a traves del method GET
@app.route('/',methods=['GET'])
def index():
    return jsonify({'message':'Welcome to my API'})