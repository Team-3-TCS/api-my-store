from .. import db


class Vendedor(db.Model):
    id_vendedor = db.Column(db.Integer, primary_key=True)
    paterno = db.Column(db.String(50))
    materno = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    telefono = db.Column(db.String(10))
    dni = db.Column(db.String(10))
    producto = db.relationship('Producto', backref='categoria', lazy=True)
    compra = db.relationship(
        'Compra', backref='vendedor', lazy=True)


def __repr__(self):
    return "<Vendedor '{}'>".format(self.id_vendedor)
