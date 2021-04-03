class modalidad:
    def __init__(self,modalidad_entrega,nombre,descripcion):
        self.modalidad_entrega=modalidad_entrega
        self.nombre=nombre
        self.descripcion=descripcion
        
modalidad1=modalidad(3, 'presencial', 'puro cigarro')
print(modalidad1.nombre)
print(modalidad1.descripcion)