from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#instancia de flask, donde se le va a pasar el name
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/dbmystore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

#una clase tareas, y con un parametro del modelo que viene de la base de datos, se define que se va a 
# guardar en la base de datos
class Rol(db.Model):
    id_rol=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    descripcion=db.Column(db.String(50))
    
    def __init__(self,id_rol,nombre,descripcion):
        self.id_rol=id_rol
        self.nombre=nombre
        self.descripcion=descripcion

#lee toda la clase y apartir de eso crea tablas
db.create_all()

#creamos una clase esquema, y importamos desde ma y desde ma importamos esquema
class Rol_Schema(ma.Schema):
    class Meta:
        #definimos los campos que quiero obtener cada ves que interactue con este esquema
        fields=('id_rol','nombre','descripcion')

rol_schema=Rol_Schema()
roles_schema=Rol_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/rol',methods=['POST'])
def create_rol():
    id_rol=request.json['id_rol']
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    #creo un esquema con las variables y lo guardo en una variable new_rol
    new_rol=rol(id_rol,nombre,descripcion)
    db.session.add(new_rol)
    db.session.commit()
    return rol_schema.jsonify(new_rol)

@app.route('/rol',methods=['GET'])
def get_rol():
    all_detalles_nombres=rol.query.all()
    result=roles_schema.dump(all_detalles_nombres)
    return jsonify(result)

@app.route('/rol/<id_rol>',methods=['GET'])
def get_rol_id(id_rol):
    rol=rol.query.get(id_rol)
    return rol_schema.jsonify(rol)

#actualizar datos es con el method PUT
@app.route('/rol/<id_rol>',methods=['PUT'])
def update_rol(id_rol):
    rol=rol.query.get(id_rol)
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    #actualizamos con las variables que recibieron los datos
    rol.nombre=nombre
    rol.descripcion=descripcion
    db.session.commit()
    return rol_schema.jsonify(rol)

#ruta para eliminar con id, y el method DELETE
@app.route('/rol/<id_rol>',methods=['DELETE'])
def delete_nombre(id_rol):
    rol=rol.query.get(id_rol)
    db.session.delete(rol)
    db.session.commit()
    return rol_schema.jsonify(rol)

#creamos una ruta principal a traves del method GET
@app.route('/',methods=['GET'])
#se crea una funcion que envie un mensaje de bienvenida
def index():
    return jsonify({'message':'Welcome to my API'})

#if __name__ es cuando inicie ese programa
#iniciar app en un puerto que mostrara por consola
if __name__=="__main__":
    app.run(debug=True)