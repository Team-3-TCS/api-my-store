class estado:
    def __init__(self,id_estado,nombre,descripcion):
        self.id_estado=id_estado
        self.nombre=nombre
        self.descripcion=descripcion

estado1= estado(123,'pagado', 'ya pagado')
print(estado1.id_estado) 
print(estado1.nombre)
print(estado1.descripcion)