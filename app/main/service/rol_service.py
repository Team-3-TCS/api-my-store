from app.main import db,ma
from app.main.model.rol import Rol

class Rol_Schema(ma.Schema):
    class Meta:
        fields=('id_rol','nombre','descripcion')

rol_schema=Rol_Schema()
roles_schema=Rol_Schema(many=True)

def create_rol(data):
    new_rol = Rol(
            id_rol=data['id_rol'],
            nombre=data['nombre'],
            descripcion=data['descripcion']
        )
    db.session.add(new_rol)
    db.session.commit()
    return rol_schema.jsonify(new_rol)

def get_rol():
    return Rol.query.all()

def get_rol_id(id_rol):
    rol=Rol.query.get(id_rol)
    return rol

def update_rol(id_rol,data):
    rol=Rol.query.get(id_rol)
    nombre=data['nombre']
    descripcion=data['descripcion']
    #actualizamos con las variables que recibieron los datos
    rol.nombre=nombre
    rol.descripcion=descripcion
    db.session.commit()
    return rol

def delete_rol(id_rol):
    rol=Rol.query.get(id_rol)
    db.session.delete(rol)
    db.session.commit()
    return rol