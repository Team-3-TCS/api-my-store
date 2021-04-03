class compra:
    def __init__(self,id_compra,id_cliente,fecha,id_estado_pago,modalidad_entrega,descuento,id_estado,id_vendedor):
        self.id_compra=id_compra
        self.id_cliente=id_cliente
        self.fecha=fecha
        self.id_estado_pago=id_estado_pago
        self.modalidad_entrega=modalidad_entrega
        self.id_estado=id_estado
        self.id_vendedor=id_vendedor


compra1= compra(4, 5, '2021-02-11',12,'presenciak',13.40,45,12)
print(compra1.id_compra) 
print(compra1.id_cliente)
print(compra1.fecha)