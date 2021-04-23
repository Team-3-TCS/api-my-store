from .. import db


class Cliente(db.Model):
    __tablename__ = "cliente"
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    compra = db.relationship(
        'Compra', backref='cliente', lazy=True)
    calificacion_producto = db.relationship(
        'Calificacion_producto', backref='cliente', lazy=True)


def __repr__(self):
    return "<Cliente '{}'>".format(self.id_cliente)
