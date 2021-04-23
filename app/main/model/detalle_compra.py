from .. import db


class Detalle_compra(db.Model):
    __tablename__ = "detalle_compra"
    id_detalle_compra = db.Column(db.Integer, primary_key=True)
    compra = db.Column(db.Integer, db.ForeignKey(
        'compra.id_compra'), nullable=False)
    producto = db.Column(db.Integer, db.ForeignKey(
        'producto.id_producto'), nullable=False)
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Float)
    descuento = db.Column(db.Float)


def __repr__(self):
    return "<Detalle_compra '{}'>".format(self.id_detalle_compra)
