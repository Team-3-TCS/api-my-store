from app.main import db,ma
from app.main.model.modalidad_entrega import Modalidad_entrega

class Modalidad_entregaSchema(ma.Schema):
    class Meta:
        fields=('Modalidad_Entrega','nombre','descripcion')

modalidad_entrega_schema=Modalidad_entregaSchema()
modalidades_entregas_schema=Modalidad_entregaSchema(many=True)

def create_modalidad_entrega(data):
    new_modalidad_entrega = Modalidad_entrega(
            Modalidad_Entrega=data['Modalidad_Entrega'],
            nombre=data['nombre'],
            descripcion=data['descripcion']
        )
    db.session.add(new_modalidad_entrega)
    db.session.commit()
    return modalidad_entrega_schema.jsonify(new_modalidad_entrega)

def get_modalidad_entrega():
    return Modalidad_entrega.query.all()

def get_modalidad_entrega_id(id_modalidad_entrega):
    Modalidad_Entrega=Modalidad_entrega.query.get(id_modalidad_entrega)
    return Modalidad_Entrega

def update_modalidad_entrega(id_modalidad_entrega,data):
    modalidad_entrega=Modalidad_entrega.query.get(id_modalidad_entrega)
    nombre=data['nombre']
    descripcion=data['descripcion']
    modalidad_entrega.nombre=nombre
    modalidad_entrega.descripcion=descripcion
    db.session.commit()
    return modalidad_entrega

def delete_modalidad_entrega(id_modalidad_entrega):
    modalidad_entrega=Modalidad_entrega.query.get(id_modalidad_entrega)
    db.session.delete(modalidad_entrega)
    db.session.commit()
    return modalidad_entrega