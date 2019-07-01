# services/users/manage.py

import unittest
import coverage

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Alquiler


COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
   
    db.session.add(Cliente(nombre='Freddy', apellido="Mercury", active=True))
    db.session.add(Cliente(nombre='Leandro', apellido="Gato", active=True))
    db.session.add(Empleado(nombre='Luis', apellido="Alcantara", active=True))
    db.session.add(Empleado(nombre='Lucho', apellido="Gomes", active=True))
    db.session.add(Pelicula(nombre='Aladdín', genero="Fantasía", fecha_lanzamiento=2019-5-8, active=True))
    db.session.add(Pelicula(nombre='Toy Story 4', genero="Fantasía", fecha_lanzamiento=2019-6-11, active=True))
    db.session.add(Alquiler(fecha_alqui=2019-6-27, fecha_devol=2019-6-27, id_cliente=1, id_empleado=1, active=True))
    db.session.add(Alq_Pel(id_alquiler=1, id_pelicula=1))
    db.session.commit()


@cli.command()
def cov():
    """Ejecuta las pruebas unitarias con coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Resumen de cobertura:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


if __name__ == '__main__':
   cli()
