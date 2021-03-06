import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import cliente
from app.main.model import calificacion_producto
from app.main.model import categoria
from app.main.model import compra
from app.main.model import detalle_compra
from app.main.model import detalle_delivery_compra
from app.main.model import estado
from app.main.model import modalidad_entrega
from app.main.model import persona
from app.main.model import producto
from app.main.model import rol
from app.main.model import usuario
from app.main.model import vendedor



app = create_app(os.getenv('MYSTORE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0')


# @manager.command
# def test():
#     """Runs the unit tests."""
#     tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     return 1


if __name__ == '__main__':
    manager.run()
