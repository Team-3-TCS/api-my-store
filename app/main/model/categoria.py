from .. import db


class Categoria(db.Model):
    __tablename__ = "categoria"
    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(200))
    producto = db.relationship('Producto', backref='categoria', lazy=True)


def __repr__(self):
    return "<Categoria '{}'>".format(self.nombre)
