class usuario:
    def __init__(self,id_usuario,id_rol,contrasenia,nombre_usuario,id_estado_actividad):
        self.id_usuario=id_usuario
        self.id_rol=id_rol
        self.contrasenia=contrasenia
        self.nombre_usuario=nombre_usuario
        self.id_estado_actividad=id_estado_actividad

usuario1=usuario(12,15,'123456','user01',987654)
print(usuario1.id_usuario)
print(usuario1.contrasenia)
print(usuario1.nombre_usuario)