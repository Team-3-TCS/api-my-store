from .. import db


class Compra(db.Model):
    __tablename__ = "compra"
    id_compra = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer)
    id_vendedor = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)
    id_Estado_compra = db.Column(db.Integer)
    id_Estado_pago = db.Column(db.Integer)
    id_modalidad_entrega = db.Column(db.Integer)
    descuento = db.Column(db.Float)
    id_estado = db.Column(db.Integer)


def __repr__(self):
    return "<Compra '{}'>".format(self.id_compra)
