from .. import db

#una clase tareas, y con un parametro del modelo que viene de la base de datos, se define que se va a 
# guardar en la base de datos
class Rol(db.Model):
    id_rol=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    descripcion=db.Column(db.String(200))
    
def __repr__(self):
    return "<Rol'{}'>".format(self.id_rol)