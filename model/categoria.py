from conexion import *
class categoria:
    id_categoria=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.Integer)
    descripcion=db.Column(db.Integer)


    def __init__(self,id_categoria,nombre,descripcion):
        self.id_categoria=id_categoria
        self.nombre=nombre
        self.descripcion=descripcion

db.create_all()

class   Categoria_Schema(ma.Schema):
    class Meta:
        fields=('id_categoria','nombre','descripcion')

categoria_schema=Categoria_Schema()
categorias_schema=Categoria_Schema(many=True)

#creamos una ruta para agregar datos de categorias
@app.route('/categoria',methods=['POST'])
def create_categoria():
    id_categoria=request.json['id_categoria']
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    new_categoria=Vendedor(id_categoria,nombre,descripcion)
    db.session.add(new_categoria)
    db.session.commit()
    return categoria_schema.jsonify(new_categoria)

    #crearemos una ruta para mostrar datos del vendedor
app.route('/categoria',methods=['GET'])
def get_categoria():
    all_categorias=Categoria.query.all()
    result=categorias_schema.dump(all_categorias)
    return jsonify(result)


@app.route('/vendedor/<id_categoria>',methods=['GET'])
def get_categoria_id(id_categoria):
    categoria=Categoria.query.get(id_categoria)
    return categoria.jsonify(categoria)
    
@app.route('/vendedor/<nombre>',methods=['GET'])
def get_categoria_nombre(nombre):
    categoria=Categoria.query.get(nombre)
    return categoria_schema.jsonify(categoria)


#actualizar datos del vendedor
@app.route('/vendedor/<id_categoria>',methods=['PUT'])
def edit_categoria(id_categoria):
    categoria=Categoria.query.get(id_categoria)
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    categoria.nombre=nombre
    categoria.descripcion=descripcion 
    db.session.commit()
    return categoria_schema.jsonify(categoria)
    return jsonify({'message':'Datos modificados'})

@app.route('/vendedor/<nombre>',methods=['PUT'])
def edit_categoria_nom(nombre):
    categoria=Categoria.query.get(nombre)
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    categoria.nombre=nombre
    categoria.descripcion=descripcion 
    db.session.commit()
    return categoria_schema.jsonify(categoria)
    return jsonify({'message':'Datos modificados'})

#ruta para eliminar con id, y el method DELETE
@app.route('/compra/<id_categoria>',methods=['DELETE'])
def delete_categoria(id_categoria):
    categoria=Categoria.query.get(id_categoria)
    db.session.delete(categoria)
    db.session.commit()
    return categoria_schema.jsonify(categoria)
    return jsonify({'message':'datos eliminados'})

@app.route('/compra/<nombre>',methods=['DELETE'])
def delete_categoria_nom(nombre):
    categoria=Categoria.query.get(nombre)
    db.session.delete(categoria)
    db.session.commit()
    return categoria_schema.jsonify(categoria)
    return jsonify({'message':'datos eliminados'})

#creamos una ruta principal a traves del method GET
@app.route('/',methods=['GET'])
def index():
    return jsonify({'message':'Welcome to my API'})

