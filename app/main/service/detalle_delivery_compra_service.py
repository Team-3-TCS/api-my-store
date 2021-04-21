from app.main import db,ma
from app.main.model.detalle_delivery_compra import Detalle_delivery_compra


class Detalle_delivery_compra_Schema(ma.Schema):
    class Meta:
        #definimos los campos que quiero obtener cada ves que interactue con este esquema
        fields=('id_detalle_delivery','id_compra','id_usuario','direccion','referencia','numero_contacto')

detalle_delivery_compra_schema=Detalle_delivery_compra_Schema()
detalle_delivery_compras_schema=Detalle_delivery_compra_Schema(many=True)

def create_detalle_delivery_compra(data):
    new_detalle_delivery_compra = Detalle_delivery_compra(
            id_compra=data['id_compra'],
            id_usuario=data['id_usuario'],
            direccion=data['direccion'],
            referencia=data['referencia'],
            numero_contacto=data['numero_contacto']
        )
    db.session.add(new_detalle_delivery_compra)
    db.session.commit()
    return detalle_delivery_compra_schema.jsonify(new_detalle_delivery_compra)

def get_detalle_delivery_compra():
    return Detalle_delivery_compra.query.all()

def get_detalle_delivery_compra_id(id_detalle_delivery):
    detalle_delivery_compra=Detalle_delivery_compra.query.get(id_detalle_delivery)
    return detalle_delivery_compra

def update_detalle_delivery_compra(id_detalle_delivery,data):
    detalle_delivery_compra=Detalle_delivery_compra.query.get(id_detalle_delivery)
    id_compra=data['id_compra']
    id_usuario=data['id_usuario']
    direccion=data['direccion']
    referencia=data['referencia']
    numero_contacto=data['numero_contacto']
    detalle_delivery_compra.id_compra=id_compra
    detalle_delivery_compra.id_usuario=id_usuario
    detalle_delivery_compra.direccion=direccion
    detalle_delivery_compra.referencia=referencia
    detalle_delivery_compra.numero_contacto=numero_contacto
    db.session.commit()
    return detalle_delivery_compra

def delete_detalle_delivery_compra(id_detalle_delivery):
    detalle_delivery_compra=Detalle_delivery_compra.query.get(id_detalle_delivery)
    db.session.delete(detalle_delivery_compra)
    db.session.commit()
    return detalle_delivery_compra