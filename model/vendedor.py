class vendedor:
    def __init__(self,id_vendedor,paterno,materno,nombre,telefono,dni):
        self.id_vendedor=id_vendedor
        self.paterno=paterno
        self.materno=materno
        self.nombre=nombre
        self.telefono=telefono
        self.dni=dni


vendedor1= vendedor(123, 'mejia', 'cuellar', 'paul', 123, 7894562)
print(vendedor1.nombre) 
print(vendedor1.paterno)
print(vendedor1.materno)