from app.main import db,ma
from app.main.model.usuario import Usuario

class Usuario_Schema(ma.Schema):
    class Meta:
        fields=('id_usuario','rol','contrasenia','nombre_usuario','id_estado_actividad')

usuario_schema=Usuario_Schema()
usuarios_schema=Usuario_Schema(many=True)

def create_usuario(data):
    new_usuario = Usuario(
            rol=data['rol'],
            contrasenia=data['contrasenia'],
            nombre_usuario=data['nombre_usuario'],
            id_estado_actividad=data['id_estado_actividad']
        )
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)

def get_usuario():
    return Usuario.query.all()

def get_usuario_id(id_usuario):
    usuario=Usuario.query.get(id_usuario)
    return usuario

def update_usuario(id_usuario,data):
    usuario=Usuario.query.get(id_usuario)
    rol=data['rol']
    contrasenia=data['contrasenia']
    nombre_usuario=data['nombre_usuario']
    id_estado_actividad=data['id_estado_actividad']
    usuario.rol=rol
    usuario.contrasenia=contrasenia
    usuario.nombre_usuario=nombre_usuario
    usuario.id_estado_actividad=id_estado_actividad
    db.session.commit()
    return usuario

def delete_usuario(id_usuario):
    usuario=Usuario.query.get(id_usuario)
    db.session.delete(usuario)
    db.session.commit()
    return usuario