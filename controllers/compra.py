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
class Compra(db.Model):
    id_compra=db.Column(db.Integer,primary_key=True)
    id_cliente=db.Column(db.Integer)
    id_vendedor=db.Column(db.Integer)
    fecha=db.Column(db.DateTime)
    id_Estado_compra=db.Column(db.Integer)
    id_Estado_pago=db.Column(db.Integer)
    Modalidad_entrega=db.Column(db.Integer)
    descuento=db.Column(db.Float)
    id_estado=db.Column(db.Integer)
    
    def __init__(self,id_compra,id_cliente,id_vendedor,fecha,id_Estado_compra,id_Estado_pago,Modalidad_entrega,descuento,id_estado):
        self.id_compra=id_compra
        self.id_cliente=id_cliente
        self.id_vendedor=id_vendedor
        self.fecha=fecha
        self.id_Estado_compra=id_Estado_compra
        self.id_Estado_pago=id_Estado_pago
        self.Modalidad_entrega=Modalidad_entrega
        self.descuento=descuento
        self.id_estado=id_estado

#lee toda la clase y apartir de eso crea tablas
db.create_all()

#creamos una clase esquema, y importamos desde ma y desde ma importamos esquema
class Compra_Schema(ma.Schema):
    class Meta:
        #definimos los campos que quiero obtener cada ves que interactue con este esquema
        fields=('id_compra','id_cliente','id_vendedor','fecha','id_Estado_compra','id_Estado_pago','Modalidad_entrega','descuento','id_estado')

compra_schema=Compra_Schema()
compras_schema=Compra_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/compra',methods=['POST'])
def create_compra():
    id_compra=request.json['id_compra']
    id_cliente=request.json['id_cliente']
    id_vendedor=request.json['id_vendedor']
    fecha=request.json['fecha']
    id_Estado_compra=request.json['id_Estado_compra']
    id_Estado_pago=request.json['id_Estado_pago']
    Modalidad_entrega=request.json['Modalidad_entrega']
    descuento=request.json['descuento']
    id_estado=request.json['id_estado']
    #creo un esquema con las variables y lo guardo en una variable new_task
    new_compra=Compra(id_compra,id_cliente,id_vendedor,fecha,id_Estado_compra,id_Estado_pago,Modalidad_entrega,descuento,id_estado)
    db.session.add(new_compra)
    db.session.commit()
    return compra_schema.jsonify(new_compra)

@app.route('/compra',methods=['GET'])
def get_compra():
    all_compras=Compra.query.all()
    result=compras_schema.dump(all_compras)
    return jsonify(result)

@app.route('/compra/<id_compra>',methods=['GET'])
def get_compra_id(id_compra):
    compra=Compra.query.get(id_compra)
    return compra_schema.jsonify(compra)

#actualizar datos es con el method PUT
@app.route('/compra/<id_compra>',methods=['PUT'])
def update_compra(id_compra):
    compra=Compra.query.get(id_compra)
    id_cliente=request.json['id_cliente']
    id_vendedor=request.json['id_vendedor']
    fecha=request.json['fecha']
    id_Estado_compra=request.json['id_Estado_compra']
    id_Estado_pago=request.json['id_Estado_pago']
    Modalidad_entrega=request.json['Modalidad_entrega']
    descuento=request.json['descuento']
    id_estado=request.json['id_estado']
    #actualizamos con las variables que recibieron los datos
    compra.id_cliente=id_cliente
    compra.id_vendedor=id_vendedor
    compra.fecha=fecha
    compra.id_Estado_compra=id_Estado_compra
    compra.id_Estado_pago=id_Estado_pago
    compra.Modalidad_entrega=Modalidad_entrega
    compra.descuento=descuento
    compra.id_estado=id_estado
    db.session.commit()
    return compra_schema.jsonify(compra)

#ruta para eliminar con id, y el method DELETE
@app.route('/compra/<id_compra>',methods=['DELETE'])
def delete_compra(id_compra):
    compra=Compra.query.get(id_compra)
    db.session.delete(compra)
    db.session.commit()
    return compra_schema.jsonify(compra)

#creamos una ruta principal a traves del method GET
@app.route('/',methods=['GET'])
#se crea una funcion que envie un mensaje de bienvenida
def index():
    return jsonify({'message':'Welcome to my API'})

#if __name__ es cuando inicie ese programa
#iniciar app en un puerto que mostrara por consola
if __name__=="__main__":
    app.run(debug=True)
