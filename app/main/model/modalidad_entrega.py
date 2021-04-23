from .. import db


class Modalidad_entrega(db.Model):
    __tablename__ = "modalidad_entrega"
    id_modalidad_entrega = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(200))
    compra = db.relationship(
        'Compra', backref='modalidad_entrega', lazy=True)


def __repr__(self):
    return "<Modalidad_entrega'{}'>".format(self.id_modalidad_entrega)
