from app.main import db,ma
from app.main.model.vendedor import Vendedor

class   Vendedor_Schema(ma.Schema):
    class Meta:
        fields=('id_vendedor','paterno','materno','nombre','telefono','dni')

vendedor_schema=Vendedor_Schema()
vendedores_schema=Vendedor_Schema(many=True)

def create_vendedor(data):
    new_vendedor = Vendedor(
            paterno=data['paterno'],
            materno=data['materno'],
            nombre=data['nombre'],
            telefono=data['telefono'],
            dni=data['dni']
        )
    db.session.add(new_vendedor)
    db.session.commit()
    return vendedor_schema.jsonify(new_vendedor)

def get_vendedor():
    return Vendedor.query.all()

def get_vendedor_id(id_vendedor):
    vendedor=Vendedor.query.get(id_vendedor)
    return vendedor

def update_vendedor(id_vendedor,data):
    vendedor=Vendedor.query.get(id_vendedor)
    paterno=data['paterno']
    materno=data['materno']
    nombre=data['nombre']
    telefono=data['telefono']
    dni=data['dni']
    vendedor.paterno=paterno
    vendedor.materno=materno 
    vendedor.nombre=nombre
    vendedor.telefono=telefono
    vendedor.dni=dni
    db.session.commit()
    return vendedor

def delete_vendedor(id_vendedor):
    vendedor=Vendedor.query.get(id_vendedor)
    db.session.delete(vendedor)
    db.session.commit()
    return vendedor