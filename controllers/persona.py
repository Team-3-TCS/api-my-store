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
class Persona(db.Model):
    id_persona=db.Column(db.Integer,primary_key=True)
    usuario=db.Column(db.Integer,db.ForeignKey('usuario.id_usuario'))
    nombre=db.Column(db.String(50))
    apellido_paterno=db.Column(db.String(50))
    apellido_materno=db.Column(db.String(50))
    correo=db.Column(db.String(50))
    celular=db.Column(db.Integer)
    genero=db.Column(db.Integer)
    
    def __init__(self,id_persona,usuario,nombre,apellido_paterno,apellido_materno,correo,celular,genero):
        self.id_persona=id_persona
        self.usuario=usuario
        self.nombre=nombre
        self.apellido_paterno=apellido_paterno
        self.apellido_materno=apellido_materno
        self.correo=correo
        self.celular=celular
        self.genero=genero

#lee toda la clase y apartir de eso crea tablas
db.create_all()

#creamos una clase esquema, y importamos desde ma y desde ma importamos esquema
class Persona_Schema(ma.Schema):
    class Meta:
        #definimos los campos que quiero obtener cada ves que interactue con este esquema
        fields=('id_persona','usuario','nombre','apellido_paterno','apellido_materno','correo','celular','genero')

persona_schema=Persona_Schema()
personas_schema=Persona_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/persona',methods=['POST'])
def create_persona():
    id_persona=request.json['id_persona']
    usuario=request.json['usuario']
    nombre=request.json['nombre']
    apellido_paterno=request.json['apellido_paterno']
    apellido_materno=request.json['apellido_materno']
    correo=request.json['correo']
    celular=request.json['celular']
    genero=request.json['genero']
    #creo un esquema con las variables y lo guardo en una variable new_task
    new_persona=Persona(id_persona,usuario,nombre,apellido_paterno,apellido_materno,correo,celular,genero)
    db.session.add(new_persona)
    db.session.commit()
    return persona_schema.jsonify(new_persona)

@app.route('/persona',methods=['GET'])
def get_persona():
    all_personas=Persona.query.all()
    result=personas_schema.dump(all_personas)
    return jsonify(result)

@app.route('/persona/<id_persona>',methods=['GET'])
def get_persona_id(id_persona):
    persona=Persona.query.get(id_persona)
    return persona_schema.jsonify(persona)

#actualizar datos es con el method PUT
@app.route('/persona/<id_persona>',methods=['PUT'])
def update_persona(id_persona):
    persona=Persona.query.get(id_persona)
    usuario=request.json['usuario']
    nombre=request.json['nombre']
    apellido_paterno=request.json['apellido_paterno']
    apellido_materno=request.json['apellido_materno']
    correo=request.json['correo']
    celular=request.json['celular']
    genero=request.json['genero']
    #actualizamos con las variables que recibieron los datos
    persona.usuario=usuario
    persona.nombre=nombre
    persona.apellido_paterno=apellido_paterno
    persona.apellido_materno=apellido_materno
    persona.correo=correo
    persona.celular=celular
    persona.genero=genero
    db.session.commit()
    return persona_schema.jsonify(persona)

#ruta para eliminar con id, y el method DELETE
@app.route('/persona/<id_persona>',methods=['DELETE'])
def delete_usuario(id_persona):
    persona=Persona.query.get(id_persona)
    db.session.delete(persona)
    db.session.commit()
    return persona_schema.jsonify(persona)

#creamos una ruta principal a traves del method GET
@app.route('/',methods=['GET'])
#se crea una funcion que envie un mensaje de bienvenida
def index():
    return jsonify({'message':'Welcome to my API'})

#if __name__ es cuando inicie ese programa
#iniciar app en un puerto que mostrara por consola
if __name__=="__main__":
    app.run(debug=True)