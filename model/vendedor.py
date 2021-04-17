from conexion import *

class Vendedor(db.Model):
    id_vendedor=db.Column(db.Integer,primary_key=True)
    paterno=db.Column(db.String(50))
    materno=db.Column(db.String(50))
    nombre=db.Column(db.String(50))
    telefono=db.Column(db.String(10))
    dni=db.Column(db.String(10))
    

    def __init__(self,id_vendedor,paterno,materno,nombre,telefono,dni):
        self.id_vendedor=id_vendedor
        self.paterno=paterno
        self.materno=materno
        self.nombre=nombre
        self.telefono=telefono
        self.dni=dni

class   Vendedor_Schema(ma.Schema):
    class Meta:
        fields=('id_vendedor','paterno','materno','nombre','telefono','dni')

vendedor_schema=Vendedor_Schema()
vendedores_schema=Vendedor_Schema(many=True)

#creamos una ruta para agregar datos de un vendedor
@app.route('/vendedor',methods=['POST'])
def create_vendedor():
    id_vendedor=request.json['id_vendedor']
    paterno=request.json['paterno']
    materno=request.json['materno']
    nombre=request.json['nombre']
    telefono=request.json['telefono']
    dni=request.json['dni']
    new_vendedor=Vendedor(id_vendedor,paterno,materno,nombre,telefono,dni)
    db.session.add(new_vendedor)
    db.session.commit()
    return vendedor_schema.jsonify(new_vendedor)

#crearemos una ruta para mostrar datos del vendedor
@app.route('/vendedor',methods=['GET'])
def get_vendedor():
    all_vendedores=Vendedor.query.all()
    result=vendedores_schema.dump(all_vendedores)
    return jsonify(result)

@app.route('/vendedor/<id_vendedor>',methods=['GET'])
def get_vendedor_id(id_vendedor):
    vendedor=Vendedor.query.get(id_vendedor)
    return vendedor_schema.jsonify(vendedor)

#actualizar datos del vendedor
@app.route('/vendedor/<id_vendedor>',methods=['PUT'])
def update_vendedor(id_vendedor):
    vendedor=Vendedor.query.get(id_vendedor)
    paterno=request.json['paterno']
    materno=request.json['materno']
    nombre=request.json['nombre']
    telefono=request.json['telefono']
    dni=request.json['dni']
    vendedor.paterno=paterno
    vendedor.materno=materno 
    vendedor.nombre=nombre
    vendedor.telefono=telefono
    vendedor.dni=dni
    db.session.commit()
    return vendedor_schema.jsonify(vendedor)
    return jsonify({'message':'Datos modificados'})

#ruta para eliminar con id, y el method DELETE
@app.route('/vendedor/<id_vendedor>',methods=['DELETE'])
def delete_vendedor(id_vendedor):
    vendedor=Vendedor.query.get(id_vendedor)
    db.session.delete(vendedor)
    db.session.commit()
    return vendedor_schema.jsonify(vendedor)
    return jsonify({'message':'datos eliminados'})