from app.main import db,ma
from app.main.model.persona import Persona

class Persona_Schema(ma.Schema):
    class Meta:
        fields=('id_persona','usuario','nombre','apellido_paterno','apellido_materno','correo','celular','genero')

persona_schema=Persona_Schema()
personas_schema=Persona_Schema(many=True)

def create_persona(data):
    new_persona = Persona(
            usuario=data['usuario'],
            nombre=data['nombre'],
            apellido_paterno=data['apellido_paterno'],
            apellido_materno=data['apellido_materno'],
            correo=data['correo'],
            celular=data['celular'],
            genero=data['genero']
        )
    db.session.add(new_persona)
    db.session.commit()
    return persona_schema.jsonify(new_persona)

def get_persona():
    return Persona.query.all()

def get_persona_id(id_persona):
    persona=Persona.query.get(id_persona)
    return persona

def update_persona(id_persona,data):
    persona=Persona.query.get(id_persona)
    usuario=data['usuario']
    nombre=data['nombre']
    apellido_paterno=data['apellido_paterno']
    apellido_materno=data['apellido_materno']
    correo=data['correo']
    celular=data['celular']
    genero=data['genero']
    #actualizamos con las variables que recibieron los datos
    persona.usuario=usuario
    persona.nombre=nombre
    persona.apellido_paterno=apellido_paterno
    persona.apellido_materno=apellido_materno
    persona.correo=correo
    persona.celular=celular
    persona.genero=genero
    db.session.commit()
    return persona

def delete_persona(id_persona):
    persona=Persona.query.get(id_persona)
    db.session.delete(persona)
    db.session.commit()
    return persona