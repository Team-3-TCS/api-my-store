class producto:
    def __init__(self,id_producto,id_categoria,id_vendedor,nombre,descripcion,precio,imagen,stock,estado_activacion,fecha_adicion,fecha_modificacion):
        self.id_producto=id_producto
        self.id_categoria=id_categoria
        self.id_vendedor=id_vendedor
        self.nombre=nombre
        self.descripcion=descripcion
        self.precio=precio
        self.imagen=imagen
        self.stock=stock
        self.estado_activacion=estado_activacion
        self.fecha_adicion=fecha_adicion
        self.fecha_modificacion=fecha_modificacion


producto1= producto(3, 4, 5,'paul','ola munda',13.40,'ksdaids',12,True,'2021-02-11','2019-10-09')
print(producto1.nombre) 
print(producto1.descripcion)
print(producto1.stock)