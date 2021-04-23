from .. import db


class Calificacion_producto(db.Model):
    __tablename__ = "calificacion_producto"
    id_calificacion = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    id_producto = db.Column(db.Integer, db.ForeignKey(
        'producto.id_producto'), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey(
        'cliente.id_cliente'), nullable=False)
    puntuacion = db.Column(db.Integer)
    comentario = db.Column(db.String(200))


def __repr__(self):
    return "<Calificacion_producto '{}'>".format(self.id_producto)
