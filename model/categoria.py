class categoria:
    def __init__(self,id_categoria,nombre,descripcion):
        self.id_categoria=id_categoria
        self.nombre=nombre
        self.descripcion=descripcion

categoria1=categoria(3, 'motos', 'calidaddelproducto')
print(categoria1.nombre)
print(categoria1.descripcion)

