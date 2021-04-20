from .. import db

class Detalle_delivery_compra(db.Model):
    id_detalle_delivery=db.Column(db.Integer,primary_key=True)
    id_compra=db.Column(db.Integer)
    id_usuario=db.Column(db.Integer)
    direccion=db.Column(db.String(100))
    referencia=db.Column(db.String(100))
    numero_contacto=db.Column(db.String(45))

def __repr__(self):
    return "<Detalle_delivery_compra'{}'>".format(self.id_detalle_delivery)

