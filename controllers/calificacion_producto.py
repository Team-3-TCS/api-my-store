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
class Calificacion_producto(db.Model):
    id_calificacion=db.Column(db.Integer,primary_key=True)
    id_producto=db.Column(db.Integer,db.ForeignKey('producto.id_producto'))
    id_cliente=db.Column(db.Integer,db.ForeignKey('cliente.id_cliente'))
    puntuacion=db.Column(db.Integer)
    comentario=db.Column(db.String(200))
    
    def __init__(self,id_calificacion,id_producto,id_cliente,puntuacion,comentario):
        self.id_calificacion=id_calificacion
        self.id_producto=id_producto
        self.id_cliente=id_cliente
        self.puntuacion=puntuacion
        self.comentario=comentario

#lee toda la clase y apartir de eso crea tablas
db.create_all()

#creamos una clase esquema, y importamos desde ma y desde ma importamos esquema
class Calificacion_producto_Schema(ma.Schema):
    class Meta:
        #definimos los campos que quiero obtener cada ves que interactue con este esquema
        fields=('id_calificacion','id_producto','id_cliente','puntuacion','comentario')

calificacion_producto_schema=Calificacion_producto_Schema()
calificacion_productos_schema=Calificacion_producto_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/calificacion_producto',methods=['POST'])
def create_calificacion_producto():
    id_calificacion=request.json['id_calificacion']
    id_producto=request.json['id_producto']
    id_cliente=request.json['id_cliente']
    puntuacion=request.json['puntuacion']
    comentario=request.json['comentario']
    #creo un esquema con las variables y lo guardo en una variable new_task
    new_calificacion_producto=Calificacion_producto(id_calificacion,id_producto,id_cliente,puntuacion,comentario)
    db.session.add(new_calificacion_producto)
    db.session.commit()
    return calificacion_producto_schema.jsonify(new_calificacion_producto)

@app.route('/calificacion_producto',methods=['GET'])
def get_calificacion_producto():
    all_calificacion_productos=Calificacion_producto.query.all()
    result=calificacion_productos_schema.dump(all_calificacion_productos)
    return jsonify(result)

@app.route('/calificacion_producto/<id_calificacion>',methods=['GET'])
def get_calificacion_producto_id(id_calificacion):
    calificacion_producto=Calificacion_producto.query.get(id_calificacion)
    return calificacion_producto_schema.jsonify(calificacion_producto)

#actualizar datos es con el method PUT
@app.route('/calificacion_producto/<id_calificacion>',methods=['PUT'])
def update_calificacion_producto(id_calificacion):
    calificacion_producto=Calificacion_producto.query.get(id_calificacion)
    id_producto=request.json['id_producto']
    id_cliente=request.json['id_cliente']
    puntuacion=request.json['puntuacion']
    comentario=request.json['comentario']
    #actualizamos con las variables que recibieron los datos
    calificacion_producto.id_producto=id_producto
    calificacion_producto.id_cliente=id_cliente
    calificacion_producto.puntuacion=puntuacion
    calificacion_producto.comentario=comentario
    db.session.commit()
    return calificacion_producto_schema.jsonify(calificacion_producto)

#ruta para eliminar con id, y el method DELETE
@app.route('/calificacion_producto/<id_calificacion>',methods=['DELETE'])
def delete_compra(id_calificacion):
    calificacion_producto=Calificacion_producto.query.get(id_calificacion)
    db.session.delete(calificacion_producto)
    db.session.commit()
    return calificacion_producto_schema.jsonify(calificacion_producto)

#creamos una ruta principal a traves del method GET
@app.route('/',methods=['GET'])
#se crea una funcion que envie un mensaje de bienvenida
def index():
    return jsonify({'message':'Welcome to my API'})

#if __name__ es cuando inicie ese programa
#iniciar app en un puerto que mostrara por consola
if __name__=="__main__":
    app.run(debug=True)