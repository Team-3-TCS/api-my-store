from .. import db

#una clase tareas, y con un parametro del modelo que viene de la base de datos, se define que se va a 
# guardar en la base de datos
class Persona(db.Model):
    id_persona=db.Column(db.Integer,primary_key=True)
    usuario=db.Column(db.Integer)
    nombre=db.Column(db.String(50))
    apellido_paterno=db.Column(db.String(50))
    apellido_materno=db.Column(db.String(50))
    correo=db.Column(db.String(100))
    celular=db.Column(db.Integer)
    genero=db.Column(db.Integer)
    
def __repr__(self):
    return "<Persona'{}'>".format(self.username)



