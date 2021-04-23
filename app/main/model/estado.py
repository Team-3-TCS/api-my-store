from .. import db

class Estado(db.Model):
    ID_ESTADO=db.Column(db.Integer,primary_key=True)
    NOMBRE=db.Column(db.String(45))
    DESCRIPCION=db.Column(db.String(200))
    compra = db.relationship(
        'Compra', backref='estado', lazy=True)

def __repr__(self):
    return "<Estado'{}'>".format(self.ID_ESTADO)
