from .. import db


class Producto(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey(
        'categoria.id_categoria'), nullable=False)
    id_vendedor = db.Column(db.Integer, db.ForeignKey(
        'vendedor.id_vendedor'), nullable=False)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(300))
    precio = db.Column(db.Float)
    imagen = db.Column(db.String(100))
    stock = db.Column(db.Integer)
    estado_activacion = db.Column(db.Integer)
    fecha_adicion = db.Column(db.DateTime)
    fecha_modificacion = db.Column(db.DateTime)
    detalle_compra = db.relationship(
        'Detalle_compra', backref='producto_detalle', lazy=True)
    calificacion_producto = db.relationship(
        'Calificacion_producto', backref='producto_calificacion', lazy=True)


def __repr__(self):
    return "<Producto'{}'>".format(self.id_producto)
