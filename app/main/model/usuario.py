from .. import db

class Usuario(db.Model):
    id_usuario=db.Column(db.Integer,primary_key=True)
    rol = db.Column(db.Integer, db.ForeignKey(
        'rol.id_rol'), nullable=False)
    contrasenia=db.Column(db.String(50))
    nombre_usuario=db.Column(db.String(50))
    id_estado_actividad=db.Column(db.Integer)
    persona = db.relationship('Persona', backref='usuario_persona', lazy=True)
    
def __repr__(self):
    return "<Usuario '{}'>".format(self.id_usuario)




