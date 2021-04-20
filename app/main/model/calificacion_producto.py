from .. import db


class Calificacion_producto(db.Model):
    __tablename__ = "calificacion_producto"
    id_calificacion = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    id_producto = db.Column(db.Integer)
    id_cliente = db.Column(db.Integer)
    puntuacion = db.Column(db.Integer)
    comentario = db.Column(db.String(200))


def __repr__(self):
    return "<Calificacion_producto '{}'>".format(self.id_producto)
