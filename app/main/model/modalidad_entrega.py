from .. import db

class Modalidad_entrega(db.Model):
    Modalidad_Entrega=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    descripcion=db.Column(db.String(200))
    
def __repr__(self):
    return "<Modalidad_entrega'{}'>".format(self.username)




