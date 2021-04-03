class detalle_delivery_compra:
    def __init__(self,id_detalle_delivery,id_compra,direccion,referencia,numero_contacto):
        self.id_detalle_delivery=id_detalle_delivery
        self.id_compra=id_compra
        self.direccion=direccion
        self.referencia=referencia
        self.numero_contacto=numero_contacto

detalle_delivery1= detalle_delivery_compra(12, 35, 'cdadasdaseae','dsaevxdf',15634)
print(detalle_delivery1.id_compra) 
print(detalle_delivery1.direccion)
print(detalle_delivery1.referencia)

