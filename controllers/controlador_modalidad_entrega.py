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
class Modalidad_entrega(db.Model):
    Modalidad_Entrega=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    descripcion=db.Column(db.String(200))
    
    def __init__(self,Modalidad_Entrega,nombre,descripcion):
        self.Modalidad_Entrega=Modalidad_Entrega
        self.nombre=nombre
        self.descripcion=descripcion

#lee toda la clase y apartir de eso crea tablas
db.create_all()

#creamos una clase esquema, y importamos desde ma y desde ma importamos esquema
class Modalidad_entregaSchema(ma.Schema):
    class Meta:
        #definimos los campos que quiero obtener cada ves que interactue con este esquema
        fields=('Modalidad_Entrega','nombre','descripcion')

#creamos una variable que es una instancia de TaskSchema
modalidad_entrega_schema=Modalidad_entregaSchema()
#creamos una instancia de la variable el many nos permite obtener multiples respuesta de la base de datos 
modalidades_entregas_schema=Modalidad_entregaSchema(many=True)

#creamos una ruta para agregar datos
@app.route('/modalidad_entrega',methods=['POST'])
def create_modalidad_entrega():
    Modalidad_Entrega=request.json['id']
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    #creo un esquema con las variables y lo guardo en una variable new_task
    new_modalidad_entrega=Modalidad_entrega(Modalidad_Entrega,nombre, descripcion)
    db.session.add(new_modalidad_entrega)
    db.session.commit()
    return modalidad_entrega_schema.jsonify(new_modalidad_entrega)

@app.route('/modalidad_entrega',methods=['GET'])
def get_modalidad_entrega():
    all_modalidades_entregas=Modalidad_entrega.query.all()
    result=modalidades_entregas_schema.dump(all_modalidades_entregas)
    #devuelve una conversion de un string a un json
    return jsonify(result)

@app.route('/modalidad_entrega/<id_modalidad_entrega>',methods=['GET'])
def get_modalidad_entrega_id(id_modalidad_entrega):
    Modalidad_Entrega=Modalidad_entrega.query.get(id_modalidad_entrega)
    return modalidad_entrega_schema.jsonify(Modalidad_Entrega)

#actualizar datos es con el method PUT
@app.route('/modalidad_entrega/<id_modalidad_entrega>',methods=['PUT'])
def update_modalidad_entrega(id_modalidad_entrega):
    #obtenemos la tarea del id que nos estan pasando y lo guardamos en la variable tarea
    modalidad_entrega=Modalidad_entrega.query.get(id_modalidad_entrega)
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    #actualizamos con las variables que recibieron los datos
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

#creamos una ruta principal a traves del method GET
@app.route('/',methods=['GET'])
#se crea una funcion que envie un mensaje de bienvenida
def index():
    return jsonify({'message':'Welcome to my API'})

#if __name__ es cuando inicie ese programa
#iniciar app en un puerto que mostrara por consola
if __name__=="__main__":
    app.run(debug=True)
