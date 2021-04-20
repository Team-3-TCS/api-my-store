from conexion import *

#una clase tareas, y con un parametro del modelo que viene de la base de datos, se define que se va a 
# guardar en la base de datos
class Usuario(db.Model):
    id_usuario=db.Column(db.Integer,primary_key=True)
    rol=db.Column(db.Integer)
    contrasenia=db.Column(db.String(50))
    nombre_usuario=db.Column(db.String(50))
    id_estado_actividad=db.Column(db.Integer)
    
    def __init__(self,id_usuario,rol,contrasenia,nombre_usuario,id_estado_actividad):
        self.id_usuario=id_usuario
        self.rol=rol
        self.contrasenia=contrasenia
        self.nombre_usuario=nombre_usuario
        self.id_estado_actividad=id_estado_actividad

#lee toda la clase y apartir de eso crea tablas
#db.create_all()

#creamos una clase esquema, y importamos desde ma y desde ma importamos esquema
class Usuario_Schema(ma.Schema):
    class Meta:
        #definimos los campos que quiero obtener cada ves que interactue con este esquema
        fields=('id_usuario','rol','contrasenia','nombre_usuario','id_estado_actividad')

usuario_schema=Usuario_Schema()
usuarios_schema=Usuario_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/usuario',methods=['POST'])
def create_usuario():
    id_usuario=request.json['id_usuario']
    rol=request.json['rol']
    contrasenia=request.json['contrasenia']
    nombre_usuario=request.json['nombre_usuario']
    id_estado_actividad=request.json['id_estado_actividad']
    #creo un esquema con las variables y lo guardo en una variable new_task
    new_usuario=Usuario(id_usuario,rol,contrasenia,nombre_usuario,id_estado_actividad)
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)

@app.route('/usuario',methods=['GET'])
def get_usuario():
    all_usuarios=Usuario.query.all()
    result=usuarios_schema.dump(all_usuarios)
    return jsonify(result)

@app.route('/usuario/<id_usuario>',methods=['GET'])
def get_usuario_id(id_usuario):
    usuario=Usuario.query.get(id_usuario)
    return usuario_schema.jsonify(usuario)

#actualizar datos es con el method PUT
@app.route('/usuario/<id_usuario>',methods=['PUT'])
def update_usuario(id_usuario):
    usuario=Usuario.query.get(id_usuario)
    rol=request.json['rol']
    contrasenia=request.json['contrasenia']
    nombre_usuario=request.json['nombre_usuario']
    id_estado_actividad=request.json['id_estado_actividad']
    #actualizamos con las variables que recibieron los datos
    usuario.rol=rol
    usuario.contrasenia=contrasenia
    usuario.nombre_usuario=nombre_usuario
    usuario.id_estado_actividad=id_estado_actividad
    db.session.commit()
    return usuario_schema.jsonify(usuario)

#ruta para eliminar con id, y el method DELETE
@app.route('/usuario/<id_usuario>',methods=['DELETE'])
def delete_usuario(id_usuario):
    usuario=Usuario.query.get(id_usuario)
    db.session.delete(usuario)
    db.session.commit()
    return usuario_schema.jsonify(usuario)