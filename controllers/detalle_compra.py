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
class Detalle_compra(db.Model):
    id_detalle_compra=db.Column(db.Integer,primary_key=True)
    compra=db.Column(db.Integer)
    producto=db.Column(db.Integer)
    cantidad=db.Column(db.Integer)
    precio=db.Column(db.Float)
    descuento=db.Column(db.Float)
    
    def __init__(self,id_detalle_compra,compra,producto,cantidad,precio,descuento):
        self.id_detalle_compra=id_detalle_compra
        self.compra=compra
        self.producto=producto
        self.cantidad=cantidad
        self.precio=precio
        self.descuento=descuento

#lee toda la clase y apartir de eso crea tablas
db.create_all()

#creamos una clase esquema, y importamos desde ma y desde ma importamos esquema
class Detalle_compra_Schema(ma.Schema):
    class Meta:
        #definimos los campos que quiero obtener cada ves que interactue con este esquema
        fields=('id_detalle_compra','compra','producto','cantidad','precio','descuento')

detalle_compra_schema=Detalle_compra_Schema()
detalles_compras_schema=Detalle_compra_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/detalle_compra',methods=['POST'])
def create_detalle_compra():
    id_detalle_compra=request.json['id_detalle_compra']
    compra=request.json['compra']
    producto=request.json['producto']
    cantidad=request.json['cantidad']
    precio=request.json['precio']
    descuento=request.json['descuento']
    #creo un esquema con las variables y lo guardo en una variable new_task
    new_detalle_compra=Detalle_compra(id_detalle_compra,compra,producto,cantidad,precio,descuento)
    db.session.add(new_detalle_compra)
    db.session.commit()
    return detalle_compra_schema.jsonify(new_detalle_compra)

@app.route('/detalle_compra',methods=['GET'])
def get_detalle_compra():
    all_detalles_compras=Detalle_compra.query.all()
    result=detalles_compras_schema.dump(all_detalles_compras)
    return jsonify(result)

@app.route('/detalle_compra/<id_detalle_compra>',methods=['GET'])
def get_detalle_compra_id(id_detalle_compra):
    detalle_compra=Detalle_compra.query.get(id_detalle_compra)
    return detalle_compra_schema.jsonify(detalle_compra)

#actualizar datos es con el method PUT
@app.route('/detalle_compra/<id_detalle_compra>',methods=['PUT'])
def update_detalle_compra(id_detalle_compra):
    detalle_compra=Detalle_compra.query.get(id_detalle_compra)
    compra=request.json['compra']
    producto=request.json['producto']
    cantidad=request.json['cantidad']
    precio=request.json['precio']
    descuento=request.json['descuento']
    #actualizamos con las variables que recibieron los datos
    detalle_compra.compra=compra
    detalle_compra.producto=producto
    detalle_compra.cantidad=cantidad
    detalle_compra.precio=precio
    detalle_compra.descuento=descuento
    db.session.commit()
    return detalle_compra_schema.jsonify(detalle_compra)

#ruta para eliminar con id, y el method DELETE
@app.route('/detalle_compra/<id_detalle_compra>',methods=['DELETE'])
def delete_compra(id_detalle_compra):
    detalle_compra=Detalle_compra.query.get(id_detalle_compra)
    db.session.delete(detalle_compra)
    db.session.commit()
    return detalle_compra_schema.jsonify(detalle_compra)

#creamos una ruta principal a traves del method GET
@app.route('/',methods=['GET'])
#se crea una funcion que envie un mensaje de bienvenida
def index():
    return jsonify({'message':'Welcome to my API'})

#if __name__ es cuando inicie ese programa
#iniciar app en un puerto que mostrara por consola
if __name__=="__main__":
    app.run(debug=True)