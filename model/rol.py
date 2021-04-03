class rol:
    def __init__(self,id_rol,nombre,descripcion):
        self.id_rol=id_rol
        self.nombre=nombre
        self.descripcion=descripcion

rol1=rol(12, 'carros', 'calidaddelproducto')
print(rol1.nombre)
print(rol1.descripcion)