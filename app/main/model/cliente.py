from .. import db

class Cliente(db.Model):
    __tablename__ = "cliente"
    id_cliente = db.Column(db.Integer, primary_key=True)


def __repr__(self):
    return "<Cliente '{}'>".format(self.username)
