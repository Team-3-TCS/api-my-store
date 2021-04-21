from app.main import db,ma
from app.main.model.estado import Estado

class Estado_Schema(ma.Schema):
    class Meta:
        fields=('ID_ESTADO','NOMBRE','DESCRIPCION')

estado_schema=Estado_Schema()
estados_schema=Estado_Schema(many=True)

def create_estado(data):
    new_estado = Estado(
            NOMBRE=data['NOMBRE'],
            DESCRIPCION=data['DESCRIPCION']
        )
    db.session.add(new_estado)
    db.session.commit()
    return estado_schema.jsonify(new_estado)

def get_estado():
    return Estado.query.all()
    #result=estados_schema.dump(all_estados)
    #return jsonify(result)

def get_estado_id(ID_ESTADO):
    estado=Estado.query.get(ID_ESTADO)
    return estado

def update_estado(ID_ESTADO,data):
    estado=Estado.query.get(ID_ESTADO)
    NOMBRE=data['NOMBRE']
    DESCRIPCION=data['DESCRIPCION']
    estado.NOMBRE=NOMBRE
    estado.DESCRIPCION=DESCRIPCION
    db.session.commit()
    return estado

def delete_estado(ID_ESTADO):
    estado=Estado.query.get(ID_ESTADO)
    db.session.delete(estado)
    db.session.commit()
    return estado