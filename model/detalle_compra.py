class detalle_compra:
    def __init__(self,id_detalle_compra,compra,producto,cantidad):
        self.id_detalle_compra=id_detalle_compra
        self.compra=compra
        self.producto=producto
        self.cantidad=cantidad

detalle1= detalle_compra(123, 12, 'bicicleta',76)
print(detalle1.compra) 
print(detalle1.producto)
print(detalle1.cantidad)