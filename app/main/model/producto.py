from .. import db

class Producto(db.Model):
    id_producto=db.Column(db.Integer,primary_key=True)
    id_categoria=db.Column(db.Integer)
    id_vendedor=db.Column(db.Integer)
    nombre=db.Column(db.String(100))
    descripcion=db.Column(db.String(300))
    precio=db.Column(db.Float)
    imagen=db.Column(db.String(100))
    stock=db.Column(db.Integer)
    estado_activacion=db.Column(db.Integer)
    fecha_adicion=db.Column(db.DateTime)
    fecha_modificacion=db.Column(db.DateTime)

def __repr__(self):
    return "<Producto'{}'>".format(self.id_producto)
