from .. import db


class Compra(db.Model):
    __tablename__ = "compra"
    id_compra = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey(
        'cliente.id_cliente'), nullable=False)
    id_vendedor = db.Column(db.Integer, db.ForeignKey(
        'vendedor.id_vendedor'), nullable=False)
    fecha = db.Column(db.DateTime)
    id_Estado_compra = db.Column(db.Integer, db.ForeignKey(
        'estado.ID_ESTADO'), nullable=False)
    id_Estado_pago = db.Column(db.Integer)
    id_modalidad_entrega = db.Column(db.Integer, db.ForeignKey(
        'modalidad_entrega.id_modalidad_entrega'), nullable=False)
    descuento = db.Column(db.Float)
    detalle_compra = db.relationship(
        'Detalle_compra', backref='compra', lazy=True)
    detalle_delivery_compra = db.relationship(
        'Detalle_delivery_compra', backref='compra', lazy=True)


def __repr__(self):
    return "<Compra '{}'>".format(self.id_compra)
