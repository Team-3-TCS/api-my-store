from conexion import *
class Cliente(db.Model):
    id_cliente=db.Column(db.Integer,primary_key=True)
    
    def __init__(self,id_cliente):
        self.id_cliente=id_cliente

class Cliente_Schema(ma.Schema):
    class Meta:
        fields=('id_cliente','')

cliente_schema=Cliente_Schema()
clientes_schema=Cliente_Schema(many=True)

#creamos una ruta para agregar datos
@app.route('/cliente',methods=['POST'])
def create_cliente():
    id_cliente=request.json['id_cliente']
    new_cliente=Cliente(id_cliente)
    db.session.add(new_cliente)
    db.session.commit()
    return cliente_schema.jsonify(new_cliente)

@app.route('/cliente',methods=['GET'])
def get_cliente():
    all_clientes=Cliente.query.all()
    result=clientes_schema.dump(all_clientes)
    return jsonify(result)

@app.route('/cliente/<id_cliente>',methods=['GET'])
def get_cliente_id(id_cliente):
    cliente=Cliente.query.get(id_cliente)
    return cliente_schema.jsonify(cliente)

#actualizar datos es con el method PUT
@app.route('/cliente/<id_cliente>',methods=['PUT'])
def update_cliente(id_cliente):
    cliente=Cliente.query.get(id_cliente)
    db.session.commit()
    return cliente_schema.jsonify(cliente)

#ruta para eliminar con id, y el method DELETE
@app.route('/cliente/<id_cliente>',methods=['DELETE'])
def delete_cliente(id_cliente):
    cliente=Cliente.query.get(id_cliente)
    db.session.delete(cliente)
    db.session.commit()
    return cliente_schema.jsonify(cliente)