class calificacion_producto:
    def __init__(self,id_calificacion,id_producto,id_cliente,puntuacion,comentario):
        self.id_calificacion=id_calificacion
        self.id_producto=id_producto
        self.id_cliente=id_cliente
        self.puntuacion=puntuacion
        self.comentario=comentario

calificacion_producto1=calificacion_producto(12,15,25,10, 'Ola munda xd')
print(calificacion_producto1.id_calificacion)
print(calificacion_producto1.id_producto)
print(calificacion_producto1.comentario)