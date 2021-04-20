from .. import db

class Vendedor(db.Model):
    id_vendedor=db.Column(db.Integer,primary_key=True)
    paterno=db.Column(db.String(50))
    materno=db.Column(db.String(50))
    nombre=db.Column(db.String(50))
    telefono=db.Column(db.String(10))
    dni=db.Column(db.String(10))
    
def __repr__(self):
    return "<Vendedor '{}'>".format(self.username)

