class persona:
    def __init__(self,id_persona,id_usuario,nombre,apellido_paterno,apellido_materno,correo,celular,genero):
        self.id_persona=id_persona
        self.id_usuario=id_usuario
        self.nombre=nombre
        self.apellido_paterno=apellido_paterno
        self.apellido_materno=apellido_materno
        self.correo=correo
        self.celular=celular
        self.genero=genero

persona1=persona(12,20,'pablo','peralta','perez','perez@gmail.com',987654321,'M')
print(persona1.id_usuario)
print(persona1.nombre)
print(persona1.correo)